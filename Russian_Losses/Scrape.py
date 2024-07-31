import requests
from bs4 import BeautifulSoup
import re
from datetime import date
import pandas as pd
from tabulate import tabulate
import sqlite3
import os

from twitter import extract_tweet_id, get_tweet_time

from postimg import check_for_date

link = "https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html"
P_link = requests.get(link)

scrape_date = date.today()

html = P_link.text
soup = BeautifulSoup(html, "html.parser")

records = []

# Find all span elements with the class 'mw-headline' and id 'Pistols'
span_elements = soup.find_all('span', {'class': 'mw-headline', 'id': 'Pistols'})

for span in span_elements:
    equipment_type = span.get_text(strip=True)
    parent_heading = span.find_parent('h3')

    if parent_heading:
        # Extract loss numbers from the parent h3 element
        loss_nums = parent_heading.get_text(strip=True).replace(equipment_type, '').strip()

        # Find the next <ul> element
        ul_element = parent_heading.find_next_sibling('ul')

        if ul_element:
            li_items = ul_element.find_all('li')

            for li in li_items:
                full_string = li.get_text(strip=True)

                # Extract model count and model name
                match = re.match(r'(\d+)\s*(.*?)(?=\(\d+,\s)', full_string)
                if match:
                    count = int(match.group(1))
                    model = match.group(2).strip().rstrip(':')
                else:
                    count = 0
                    model = full_string.split(':')[0]

                # Find all <a> tags with href attributes
                a_tags = li.find_all('a', href=True)
        
                for a in a_tags:
                    img_link = a['href']
                    img_desc = a.get_text(strip=True).strip('()')

                    post_time = 'N/A'  # Default value
                    if 'twitter.com' in img_link:
                        tweet_id = extract_tweet_id(img_link)
                        if tweet_id is not None:
                            post_time = get_tweet_time(tweet_id).date()
                    elif 'postimg' in img_link:
                        date_found, date_obj = check_for_date(img_link)
                        if date_found:
                            post_time = date_obj.date()
                        
                    records.append({
                        'Equipment Type': equipment_type,
                        'Model': model,
                        'Total Model Losses': count,
                        'Description': img_desc,
                        'Image Date': post_time,
                        'Image Link': img_link,
                        'Date Scraped': scrape_date
                    })

df = pd.DataFrame(records)

#print(tabulate(df.head(), headers='keys', tablefmt='psql'))

# Save the DataFrame to a SQLite database
folder_path = r"C:\Users\suici\Github\Russian_Losses"
db_filename = 'russian_loss_data.db'
table_name = 'equipment_losses'
db_full_path = os.path.join(folder_path, db_filename)

conn = sqlite3.connect(db_full_path)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.commit()
conn.close()

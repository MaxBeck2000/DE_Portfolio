import requests
from bs4 import BeautifulSoup
import re
from datetime import date
import pandas as pd
import sqlite3
import os
import csv

from twitter import extract_tweet_id, get_tweet_time
from postimg import check_for_date

# Initialize the URL and other variables
link = "https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html"
P_link = requests.get(link)

scrape_date = date.today()

html = P_link.text
soup = BeautifulSoup(html, "html.parser")

records = []
no_date = []  # Initialize outside the loop to collect all links without dates

# CSV file path for URLs without dates
csv_file_path = r'C:\Users\suici\Github\Russian_Losses\urls_without_dates.csv'

# Function to read existing URLs from the CSV file
def read_existing_urls(csv_file_path):
    if os.path.exists(csv_file_path):
        df = pd.read_csv(csv_file_path)
        return set(df['URL'].tolist())  # Return as a set for faster lookups
    return set()

# Function to append new URLs to the CSV file
def append_urls_to_csv(url_list, csv_file_path):
    existing_urls = read_existing_urls(csv_file_path)
    new_urls = [url for url in url_list if url not in existing_urls]

    if new_urls:
        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            for url in new_urls:
                writer.writerow([url])  # Write each new URL

# Read existing URLs before scraping
existing_urls = read_existing_urls(csv_file_path)

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
                    if 'twitter.com' in img_link or 'x.com' in img_link:
                        tweet_id = extract_tweet_id(img_link)
                        if tweet_id is not None:
                            post_time = get_tweet_time(tweet_id).date()
                    elif 'postimg' in img_link:
                        date_found, date_obj = check_for_date(img_link)
                        if date_found:
                            post_time = date_obj.date()
                        else:
                            if img_link not in existing_urls:
                                no_date.append(img_link)

                    records.append({
                        'Equipment Type': equipment_type,
                        'Model': model,
                        'Total Model Losses': count,
                        'Description': img_desc,
                        'Image Date': post_time,
                        'Image Link': img_link,
                        'Date Scraped': scrape_date
                    })

# Convert records to DataFrame
df = pd.DataFrame(records)

# Print URLs without date
print("URLs without date:", no_date)

# Save the DataFrame to a SQLite database
folder_path = r"C:\Users\suici\Github\Russian_Losses"
db_filename = 'russian_loss_data.db'
table_name = 'equipment_losses'
db_full_path = os.path.join(folder_path, db_filename)

conn = sqlite3.connect(db_full_path)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.commit()
conn.close()

# Append the no_date list to the CSV file
append_urls_to_csv(no_date, csv_file_path)

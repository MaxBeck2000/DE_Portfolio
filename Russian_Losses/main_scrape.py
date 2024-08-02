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

link = "https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html"
P_link = requests.get(link)

scrape_date = date.today()

html = P_link.text
soup = BeautifulSoup(html, "html.parser")

records = []
no_date = []

# CSV file path for URLs without dates
csv_file_path = r'C:\Users\suici\Github\Russian_Losses\urls_without_dates.csv'
csv_dates_found = r'C:\Users\suici\Github\Russian_Losses\extracted_image_dates.csv'



# Function to read existing URLs from the CSV file
def read_existing_urls(csv_file_path):
    if os.path.exists(csv_file_path) and os.path.getsize(csv_file_path) > 0:
        try:
            df = pd.read_csv(csv_file_path, header=None)
            return set(df[0].tolist())  # Return as a set for faster lookups
        except pd.errors.EmptyDataError:
            return set()
        except Exception as e:
            print(f"An error occurred while reading CSV: {e}")
            return set()
    return set()

def read_urls_and_dates(csv_file_path):
    if os.path.exists(csv_file_path) and os.path.getsize(csv_file_path) > 0:
        try:
            df = pd.read_csv(csv_file_path, header=None)
            # Assuming URLs are in the first column (index 0) and dates are in the second column (index 1)
            url_date_dict = dict(zip(df[0], pd.to_datetime(df[1], errors='coerce')))
            return url_date_dict
        except pd.errors.EmptyDataError:
            return {}
        except Exception as e:
            print(f"An error occurred while reading CSV: {e}")
            return {}
    return {}


# Function to append new URLs to the CSV file
def append_urls_to_csv(url_list, csv_file_path):
    existing_urls = read_existing_urls(csv_file_path)
    new_urls = [url for url in url_list if url not in existing_urls]

    if new_urls:
        try:
            with open(csv_file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                for url in new_urls:
                    writer.writerow([url])
        except Exception as e:
            print(f"An error occurred while writing to CSV: {e}")

# Read existing URLs stored in CSV before scraping
existing_urls_without_date = read_existing_urls(csv_file_path)
found_date_urls = read_urls_and_dates(csv_dates_found)
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
                    post_time = 'N/A'
                    if 'twitter.com' in img_link or 'x.com' in img_link:
                        tweet_id = extract_tweet_id(img_link)
                        if tweet_id is not None:
                            post_time = get_tweet_time(tweet_id).date()
                    elif 'postimg' in img_link:
                        date_found, date_obj = check_for_date(img_link)
                        if date_found:
                            post_time = date_obj.date()
                        elif img_link in found_date_urls:
                            post_time = found_date_urls[img_link].date()
                        else:
                            if img_link not in existing_urls_without_date:
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

df = pd.DataFrame(records)

# Save the DataFrame to a SQLite database
folder_path = r"C:\Users\suici\Github\Russian_Losses"
db_filename = 'russian_loss_data.db'
table_name = 'equipment_losses'
db_full_path = os.path.join(folder_path, db_filename)

try:
    conn = sqlite3.connect(db_full_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.commit()
finally:
    conn.close()

# Append the no_date list to the CSV file
append_urls_to_csv(no_date, csv_file_path)

# Print new URLs without date from future scrapes
print("New URLs without date:", no_date)

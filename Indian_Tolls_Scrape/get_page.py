import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
import sqlite3
from datetime import date
import os

database_dir = 'Indian_Tolls_Scrape'
database_file = 'nhai_info.db'
database_path = os.path.join(database_dir, database_file)

os.makedirs(database_dir, exist_ok=True)

conn = sqlite3.connect(database_path)


r = requests.get('https://tis.nhai.gov.in/TollInformation.aspx?TollPlazaID=5753')
soup = BeautifulSoup(r.text, 'html.parser')
plaza_name = soup.find(class_='PA15').find_all('p')[0].find('lable')
table = soup.find_all('table', class_='tollinfotbl')[0]
x = str(table)
y = pd.read_html(x)[0].dropna(axis=0, how='all') #drop rows that has NA's

cols = y.columns.tolist()
cols.insert(0, 'Date Scrapped')
cols.insert(1, 'Plaza Name')
y['Plaza Name'] = plaza_name.text
y['Date Scrapped'] = date.today()
y = y[cols]
y.rename(columns = {'Date Scrapped': 'Date Scraped'}, inplace = True)
y.to_sql('nhai_toll_info', conn, if_exists='append', index=False)

print(tabulate(y, headers = 'keys', tablefmt = 'psql', showindex=False))

conn.close()
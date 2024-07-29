import numpy as np 
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from datetime import date

link = "https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html"
P_link = requests.get(link)

scrape_date = date.today()

if P_link.status_code == 200:
    print('Scraping is allowed')
else:
    print('Scraping is not allowed on this website')

html = P_link.text
soup = BeautifulSoup(html, "html.parser")

equipment_dict = {}

span_elements = soup.find_all('span', {'class': 'mw-headline', 'id': 'Pistols'})

for span in span_elements:
    equipment_type = span.get_text(strip = True)
    for type in equipment_type:
        nums = span.find_parent('h3')
        loss_nums = nums = span.find_parent('h3').get_text(strip = True).replace(equipment_type, '').strip()
    equipment_dict[equipment_type] = loss_nums

for eq_type, losses in equipment_dict.items():
    print(f"{eq_type}:\nLosses (as of {scrape_date}) : {losses}\n{'-'*40}")

# # If the tanks section is found
# if tanks_section:
#     # Find the parent heading
#     parent_heading = tanks_section.find_parent('h3')
#     print(parent_heading.text)  # Print the heading

#     # Extract the content following the heading
#     content = []
#     sibling = parent_heading.find_next_sibling()
#     while sibling and sibling.name != 'h3':
#         content.append(sibling.get_text(strip=True))
#         sibling = sibling.find_next_sibling()

#     # Join the content list into a single string
#     tanks_content = "\n".join(content)
#     print(tanks_content)
# else:
#     print("Tanks section not found")

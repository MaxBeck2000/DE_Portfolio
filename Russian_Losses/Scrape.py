import numpy as np 
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

link = "https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html"
P_link = requests.get(link)

if P_link.status_code == 200:
    print('Scraping is allowed')
else:
    print('Scraping is not allowed on this website')

html = P_link.text
soup = BeautifulSoup(html, "html.parser")


span_elements = soup.find_all('span', {'class': 'mw-headline', 'id': 'Pistols'})

equipment_types = [span.get_text(strip=True) for span in span_elements if span.get_text(strip=True)]

print(equipment_types)


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

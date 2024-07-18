import numpy as np 
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

link = "https://www.holidify.com/explore/"
P_link = requests.get(link)
if P_link.status_code == 200:
    print('Scraping is allowed')
else:
    print('Scraping is not allowed on this website')

P_html = P_link.text
P_soup = BeautifulSoup(P_html, "html.parser")

containers = P_soup.findAll("div", {"class" : "col-12 col-md-6 pr-md-3"})

print(len(containers))

pattern = r'(\d+)\.\s+([^-\n]+)\s*(?:-\s*(.*))?'
#(\d+): Captures one or more digits.
#\.: Matches the literal dot after the number.
#\s+: Matches one or more whitespace characters.
#([^-\n]+): Captures the country name, which consists of any characters except the dash (-) or newline (\n).
#\s+-\s+: Matches the dash surrounded by spaces.
#(.*): Captures the rest of the line, which is the description.
#(?:-\s*(.*))? part matches the dash and the description if present but does not fail if they are missing.
ranks = []
countries = []
descriptions = []

for container in containers:
    p_line = container.find("h3", {"class":"card-heading"})
    if p_line:
        text_content = p_line.get_text(strip = True)
        match = re.search(pattern, text_content)

        if match:
            rank = match.group(1)
            country = match.group(2).strip() 
            description = match.group(3).strip() if match.group(3) else 'N/A'
            ranks.append(rank)
            countries.append(country)
            descriptions.append(description)
        
country_ranks = pd.DataFrame({'Rank': ranks,
                              'Country': countries,
                              'Description': descriptions})

print(tabulate(country_ranks, headers = 'keys', tablefmt = 'psql', showindex=False))
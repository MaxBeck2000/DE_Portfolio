import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import re
import requests
from bs4 import BeautifulSoup

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

container = containers[0]
column = ['Country']
Places = pd.DataFrame(columns = column)

for container in containers:
    p_name = container.findAll("h3"), {"class":"card-heading"}
    p_num = 
    print(p_name)
    # p_nameN = p_name[0].text[4:].strip().split()
#print(Places.head())
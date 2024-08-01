import numpy as np 
import pandas as pd
import re
import requests
import json
from bs4 import BeautifulSoup
from tabulate import tabulate

link = "https://fantasy.premierleague.com/api/bootstrap-static/"
response = requests.get(link)
if response.status_code == 200:
    print('Scraping is allowed')
    json_data = response.json()
else:
    print('Scraping is not allowed on this website')

weeks = json_data.get('events',[])

weeknums = []
deadlines = []

for week in weeks:
    weeknum = week.get('name')
    deadline = week.get('deadline_time')
    weeknums.append(weeknum)
    deadlines.append(deadline)


Gameweeks = pd.DataFrame({'Gameweek': weeknums,
                              'Deadline': deadlines})

print(tabulate(Gameweeks, headers = 'keys', tablefmt = 'psql', showindex=False))
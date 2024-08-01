import re
from datetime import datetime

def check_for_date(url):
    #last_12_chars = url[-20:]
    date_pattern = re.compile(r'\d{2}-\d{2}-\d{2}')
    match = date_pattern.search(url)

    if match:
        date_str = match.group()
        try:
            date_obj = datetime.strptime(date_str, '%d-%m-%y')
            return True, date_obj
        except ValueError:
            return False, None
    else:
        return False, None

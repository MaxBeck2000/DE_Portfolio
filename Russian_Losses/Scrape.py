import requests
from bs4 import BeautifulSoup
import re
from datetime import date

link = "https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html"
P_link = requests.get(link)

scrape_date = date.today()

html = P_link.text
soup = BeautifulSoup(html, "html.parser")

equipment_dict = {}
span_elements = soup.find_all('span', {'class': 'mw-headline', 'id': 'Pistols'})

for span in span_elements:
    equipment_type = span.get_text(strip=True)
    parent_heading = span.find_parent('h3')

    if parent_heading:
        # Extract loss numbers from the parent h3 element
        loss_nums = parent_heading.get_text(strip=True).replace(equipment_type, '').strip()

        # Find the next <ul> element
        ul_element = parent_heading.find_next_sibling('ul')
        models = []

        if ul_element:
            li_items = ul_element.find_all('li')
            for li in li_items:
                full_string = li.get_text(strip=True)
                # print(f"Debug: Full String: {full_string}")
                match = re.search(r'^[^\d]*(.*?):', full_string)
                if match:
                    models.append(match.group(1).strip())
                #else:
                    #print(f"Debug: No match found in: {full_string}")

        equipment_dict[equipment_type] = {
            'loss_numbers': loss_nums,
            'models': models
        }
    #else:
        #print(f"Debug: No parent <h3> element found for span with text '{equipment_type}'")

for eq_type, losses in equipment_dict.items():
    print(f"{eq_type}\nLosses (as of {scrape_date}): {losses['loss_numbers']}")
    print("Models:")
    if losses['models']:
        for model in losses['models']:
            print(f"    - {model}")
    else:
        print("    No models listed.")
    print('-'*40)




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

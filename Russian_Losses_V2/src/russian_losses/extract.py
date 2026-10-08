import re

import requests
from bs4 import BeautifulSoup

ORYX_URL = (
	"https://www.oryxspioenkop.com/2022/02/"
	"attack-on-europe-documenting-equipment.html"
)

def fetch_page() -> BeautifulSoup:
	"""Download Oryx page and return parsed HTML"""

	response = requests.get(ORYX_URL, timeout = 30)
	response.raise_for_status()

	return BeautifulSoup(response.text, "html.parser")

def extract_categories(soup: BeautifulSoup) -> list[str]:
    """Extract the names of all equipment categories."""

    categories = []

    for heading in soup.find_all("h3"):

        # Find the HTML element immediately after the heading.
        next_element = heading.find_next_sibling()

        # Only equipment categories have a <ul> directly after them.
        if next_element is None or next_element.name != "ul":
            continue

        # Extract the heading's visible text.
        category_name = heading.get_text(" ", strip=True)

        # Remove the statistics in brackets.
        category_name = re.sub(
            r"\s*\(\d+,\s*of which.*\)$",
            "",
            category_name,
        ).strip()

        categories.append(category_name)

    return categories

if __name__ == "__main__":
    soup = fetch_page()
    categories = extract_categories(soup)

    print(f"Found {len(categories)} equipment categories:\n")

    for category in categories:
        print(f"- {category}")
import cv2
from PIL import Image
import re
from datetime import datetime
import requests
import numpy as np
from io import BytesIO
import csv
import easyocr

# Initialize the easyOCR reader
reader = easyocr.Reader(['en'])

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    alpha = 2.0
    beta = 0
    contrast = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)
    blurred = cv2.GaussianBlur(contrast, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh

def extract_date_from_image_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        content_type = response.headers.get('Content-Type')
        if 'image' not in content_type:
            return None, 'Not an image URL'
        
        image_bytes = BytesIO(response.content)
        img = Image.open(image_bytes)
        img_cv = np.array(img)
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)
        processed_image = preprocess_image(img_cv)
        processed_image_pil = Image.fromarray(processed_image)
        
        # Use easyOCR to extract text
        results = reader.readtext(np.array(processed_image_pil))
        text = ' '.join([result[1] for result in results])
        
        # Regex to find dates in 'dd/mm/yyyy' or 'dd.mm.yyyy' format
        match = re.search(r'\d{1,2}[./]\d{1,2}[./]\d{4}', text)
        if match:
            date_str = match.group()
            # Handle both formats: 'dd.mm.yyyy' and 'dd/m/yyyy'
            date_format = '%d.%m.%Y' if '.' in date_str else '%d/%m/%Y'
            date_obj = datetime.strptime(date_str, date_format)
            return date_obj.date(), None
        
        return None, text
    except Exception as e:
        return None, str(e)

def process_urls_to_csv(source_csv_file_path, output_csv_file_path, processed_csv_file_path, remaining_csv_file_path, batch_size):
    # Read processed URLs from the processed CSV file
    try:
        with open(processed_csv_file_path, newline='') as processed_file:
            reader = csv.reader(processed_file)
            processed_urls = {row[0] for row in reader}
    except FileNotFoundError:
        processed_urls = set()

    # Read URLs from the source CSV file
    with open(source_csv_file_path, newline='') as source_file:
        reader = csv.reader(source_file)
        url_list = [row[0] for row in reader if row[0] in processed_urls]

    # Process only the first batch_size URLs
    batch_urls = url_list[:batch_size]
    found_dates = []
    remaining_urls = []

    for url in batch_urls:
        date, text = extract_date_from_image_url(url)
        if date:
            found_dates.append([url, date])
        else:
            remaining_urls.append([url, text])

    # Append found dates to the output CSV file
    if found_dates:
        with open(output_csv_file_path, mode='a', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerows(found_dates)

    # Append remaining URLs with detected text to the remaining URLs CSV
    if remaining_urls:
        with open(remaining_csv_file_path, mode='a', newline='') as remaining_file:
            writer = csv.writer(remaining_file)
            writer.writerows(remaining_urls)

    # Update the source CSV file by removing only URLs with found dates
    remaining_urls_list = [url for url in url_list if url not in {url for url, _ in found_dates}]
    with open(source_csv_file_path, mode='w', newline='') as source_file:
        writer = csv.writer(source_file)
        for url in remaining_urls_list:
            writer.writerow([url])

    pct_found = (len(found_dates) / batch_size) * 100 if batch_size > 0 else 0
    print(f'Percentage of URLs where a date was found: {pct_found:.2f}%')

source_csv_file_path = r'C:\Users\suici\Github\Russian_Losses\urls_without_dates.csv'
output_csv_file_path = r'C:\Users\suici\Github\Russian_Losses\extracted_image_dates.csv'
processed_csv_file_path = r'C:\Users\suici\Github\Russian_Losses\processed_urls.csv'
remaining_csv_file_path = r'C:\Users\suici\Github\Russian_Losses\remaining_urls.csv'

# Process URLs and update the source and remaining CSV files
process_urls_to_csv(source_csv_file_path, output_csv_file_path, processed_csv_file_path, remaining_csv_file_path, batch_size=10)

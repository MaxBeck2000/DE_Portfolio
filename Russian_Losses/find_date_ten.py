import cv2
import pytesseract
from PIL import Image
import re
from datetime import datetime
import requests
import numpy as np
from io import BytesIO
import csv

# Configure pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path

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
            return None
        
        image_bytes = BytesIO(response.content)
        img = Image.open(image_bytes)
        img_cv = np.array(img)
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)
        processed_image = preprocess_image(img_cv)
        processed_image_pil = Image.fromarray(processed_image)
        
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(processed_image_pil, config=custom_config)
        
        match = re.search(r'\d{2}\.\d{2}\.\d{4}', text)
        if match:
            date_str = match.group()
            date_obj = datetime.strptime(date_str, '%d.%m.%Y')
            return date_obj.date()
    except Exception:
        return None
    return None

def process_urls_to_csv(source_csv_file_path, output_csv_file_path, processed_csv_file_path, batch_size=10):
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
        url_list = [row[0] for row in reader if row[0] not in processed_urls]

    # Process only the first batch_size URLs
    batch_urls = url_list[:batch_size]
    found_dates = []

    for url in batch_urls:
        date = extract_date_from_image_url(url)
        if date:
            found_dates.append([url, date])
            processed_urls.add(url)

    # Append found dates to the output CSV file
    if found_dates:
        with open(output_csv_file_path, mode='a', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerows(found_dates)

    # Update the source CSV file by removing only URLs with found dates
    remaining_urls = [url for url in url_list if url not in {url for url, _ in found_dates}]

    # Write remaining URLs back to the source CSV file
    with open(source_csv_file_path, mode='w', newline='') as source_file:
        writer = csv.writer(source_file)
        for url in remaining_urls:
            writer.writerow([url])

    # Append processed URLs to the processed CSV file
    with open(processed_csv_file_path, mode='a', newline='') as processed_file:
        writer = csv.writer(processed_file)
        for url in batch_urls:
            writer.writerow([url])

# Example usage
source_csv_file_path = r'C:\Users\suici\Github\Russian_Losses\urls_without_dates.csv'
output_csv_file_path = r'C:\Users\suici\Github\Russian_Losses\extracted_image_dates.csv'
processed_csv_file_path = r'C:\Users\suici\Github\Russian_Losses\processed_urls.csv'

# Process URLs and update the source and processed CSV files
process_urls_to_csv(source_csv_file_path, output_csv_file_path, processed_csv_file_path, batch_size=10)

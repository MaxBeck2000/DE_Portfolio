import cv2
from PIL import Image
import re
from datetime import datetime
import requests
import numpy as np
from io import BytesIO
import csv
import easyocr

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
            return None
        
        image_bytes = BytesIO(response.content)
        img = Image.open(image_bytes)
        img_cv = np.array(img)
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)
        processed_image = preprocess_image(img_cv)
        
        # Use OCR to extract text from the processed image
        text = reader.readtext(np.array(processed_image), detail=0)

        match = re.search(r'\d{1,2}[./]\d{1,2}[./]\d{4}', ' '.join(text))
        if match:
            date_str = match.group()
            # Handle both formats: 'dd.mm.yyyy' and 'dd/m/yyyy'
            date_format = '%d.%m.%Y' if '.' in date_str else '%d/%m/%Y'
            date_obj = datetime.strptime(date_str, date_format)
            return date_obj.date()
        else:
            return text  # Return the detected text if no date is found
    except Exception as e:
        print(f"Error processing {url}: {e}")
        return None

def process_urls_to_csv(source_csv_file_path, output_csv_file_path, processed_csv_file_path, remaining_csv_file_path, batch_size):
    # Read processed URLs from the processed CSV file
    try:
        with open(processed_csv_file_path, newline='') as processed_file:
            reader = csv.reader(processed_file)
            processed_urls = {row[0] for row in reader}
    except FileNotFoundError:
        processed_urls = set()

    # Read URLs from the source CSV file (unprocessed)
    with open(source_csv_file_path, newline='') as source_file:
        reader = csv.reader(source_file)
        source_urls = set(row[0] for row in reader)

    print(f"Total URLs in source: {len(source_urls)}")
    print(f"Already processed URLs: {len(processed_urls)}")

    # Select URLs that are in both the processed set and source set
    urls_to_process = [url for url in source_urls if url in processed_urls][:batch_size]

    print(f"URLs to process: {len(urls_to_process)}")

    found_dates = []
    unfound_dates = []

    for url in urls_to_process:
        result = extract_date_from_image_url(url)
        if isinstance(result, datetime):
            found_dates.append([url, result])
            processed_urls.add(url)
        elif isinstance(result, list):  # If the result is the detected text list
            unfound_dates.append([url, ' '.join(result)])  # Store the URL and detected text

    # Ensure that found dates are written to the output file
    if found_dates:
        with open(output_csv_file_path, mode='a', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerows(found_dates)
            print(f"Dates found and written: {len(found_dates)}")

    # Remove URLs with found dates from the source list before writing back
    remaining_urls = [url for url in source_urls if url not in processed_urls]

    print(f"Remaining URLs to write: {len(remaining_urls)}")

    # Update the source CSV with remaining URLs (those still without dates)
    with open(source_csv_file_path, mode='w', newline='') as source_file:  # Use write mode to overwrite the file
        writer = csv.writer(source_file)
        for url in remaining_urls:
            writer.writerow([url])

    # Append URLs with no found date but with detected text to the remaining CSV file
    if unfound_dates:
        with open(remaining_csv_file_path, mode='a', newline='') as remaining_file:
            writer = csv.writer(remaining_file)
            writer.writerows(unfound_dates)
            print(f"Unfound URLs written to remaining file: {len(unfound_dates)}")
            
    pct_found = (len(found_dates) / len(urls_to_process)) * 100 if urls_to_process else 0
    print(f'Percentage of URLs where a date was found: {pct_found:.2f}%')

# Example paths
source_csv_file_path = r'C:\Users\suici\Github\Russian_Losses\urls_without_dates.csv'
output_csv_file_path = r'C:\Users\suici\Github\Russian_Losses\extracted_image_dates.csv'
processed_csv_file_path = r'C:\Users\suici\Github\Russian_Losses\processed_urls.csv'
remaining_csv_file_path = r'C:\Users\suici\Github\Russian_Losses\remaining_urls.csv'

process_urls_to_csv(source_csv_file_path, output_csv_file_path, processed_csv_file_path, remaining_csv_file_path, batch_size=10)

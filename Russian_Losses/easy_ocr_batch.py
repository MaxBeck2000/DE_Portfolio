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

def clean_extracted_text(text):
    """
    Clean and normalize extracted text to handle common OCR errors and improve date detection.
    """
    # Replace common OCR errors
    text = text.replace('O', '0').replace('I', '1').replace('|', '1')
    
    # Remove any non-alphanumeric characters except date separators
    text = re.sub(r'[^\w\s./,-]', '', text)
    
    return text

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
        
        # Clean the extracted text
        cleaned_text = clean_extracted_text(text)
        print(f"Extracted text: {cleaned_text}")  # Debug statement

        # Regex to find various date formats, including those with commas
        date_patterns = [
            r'\b\d{1,2}[./,-]\d{1,2}[./,-]\d{4}\b',  # dd/mm/yyyy, dd-mm-yyyy, dd.mm.yyyy, dd,mm,yyyy
            r'\b\d{1,2}[./,-]\d{1,2}[./,-]\d{2}\b',  # dd/mm/yy, dd-mm-yy, dd.mm.yy, dd,mm,yy
            r'\b\d{1,2}[./,-]\d{2}[./,-]\d{2}\b',    # dd/mm/yy with two-digit year
            r'\b\d{1,2}[./,-]\d{2}\b',               # dd-mm, dd/mm, dd.mm, dd,mm
            r'\b\d{2}[./,-]\d{2}[./,-]\d{2}\b',      # mm/dd/yy (US format)
            r'\b\d{1,2}[./,-]\d{1,2}[./,-]\d{2,4}\b' # Various formats with commas
        ]
        
        for pattern in date_patterns:
            match = re.search(pattern, cleaned_text)
            if match:
                date_str = match.group()
                print(f"Matched date string: {date_str}")  # Debug statement
                
                # Normalize date_str by replacing commas with dots to standardize it
                date_str = date_str.replace(',', '.')
                
                # Handle various date formats
                date_formats = [
                    '%d-%m-%Y', '%d/%m/%Y', '%d.%m.%Y',  # Full year
                    '%d-%m-%y', '%d/%m/%y', '%d.%m.%y',  # Two-digit year
                    '%m-%d-%y', '%m/%d/%y'               # US format (optional)
                ]
                for fmt in date_formats:
                    try:
                        date_obj = datetime.strptime(date_str, fmt)
                        return date_obj.date(), None
                    except ValueError:
                        continue
        
        print(f"No valid date found in text: {cleaned_text}")  # Debug statement for missing dates
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
process_urls_to_csv(source_csv_file_path, output_csv_file_path, processed_csv_file_path, remaining_csv_file_path, batch_size=250)

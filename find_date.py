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

def process_urls_to_csv(url_list, csv_file_path):
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['URL', 'Date'])
        
        for url in url_list:
            date = extract_date_from_image_url(url)
            if date:
                writer.writerow([url, date])
            else:
                writer.writerow([url, 'Date not found'])

# Example usage
url_list = ['https://i.postimg.cc/wMqmL10f/1007-t62m-capt.jpg']  # Replace with your list of URLs
csv_file_path = 'image_dates.csv'
process_urls_to_csv(url_list, csv_file_path)

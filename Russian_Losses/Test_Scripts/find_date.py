import cv2
import pytesseract
from PIL import Image
import re
from datetime import datetime
import requests
import numpy as np
from io import BytesIO

# Configure pytesseract (update this path if needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image):
    """Preprocess the image to improve OCR accuracy."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    alpha = 2.0  # Simple contrast control
    beta = 0     # Simple brightness control
    contrast = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)
    blurred = cv2.GaussianBlur(contrast, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh

def extract_date_from_image_url(url):
    """Extract a date from an image at the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        content_type = response.headers.get('Content-Type')
        if 'image' not in content_type:
            print("URL does not point to an image.")
            return None
        
        image_bytes = BytesIO(response.content)
        img = Image.open(image_bytes)
        img_cv = np.array(img)
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)
        processed_image = preprocess_image(img_cv)
        processed_image_pil = Image.fromarray(processed_image)
        
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(processed_image_pil, config=custom_config)
        
        # Match both 'dd.mm.yyyy' and 'dd/m/yyyy' formats
        match = re.search(r'\d{1,2}[./]\d{1,2}[./]\d{4}', text)
        if match:
            date_str = match.group()
            # Handle both formats: 'dd.mm.yyyy' and 'dd/m/yyyy'
            date_format = '%d.%m.%Y' if '.' in date_str else '%d/%m/%Y'
            date_obj = datetime.strptime(date_str, date_format)
            return date_obj.date()
        else:
            print("Date not found in the image.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    return None

# Enter the URL to process
image_url = 'https://i.postimg.cc/V648Y3sp/436.png'  # Replace with your image URL

# Process the image URL and print the extracted date
extracted_date = extract_date_from_image_url(image_url)
if extracted_date:
    print(f"Extracted date: {extracted_date}")
else:
    print("No date extracted.")

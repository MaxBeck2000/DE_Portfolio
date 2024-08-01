import cv2
import pytesseract
from PIL import Image
import re
from datetime import datetime
import requests
import numpy as np
from io import BytesIO

# Configure pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path based on your installation

def extract_date_from_image_url(url):
    try:
        # Download the image
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        
        # Check Content-Type to ensure it's an image
        content_type = response.headers.get('Content-Type')
        if 'image' not in content_type:
            return None
        
        # Load image data into BytesIO
        image_bytes = BytesIO(response.content)
        
        # Open image with PIL
        img = Image.open(image_bytes)
        
        # Convert PIL image to OpenCV format
        img_cv = np.array(img)
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)
        
        # Preprocess the image
        processed_image = preprocess_image(img_cv)
        
        # Convert the processed image to PIL format for pytesseract
        processed_image_pil = Image.fromarray(processed_image)
        
        # Define OCR configuration
        custom_config = r'--oem 3 --psm 6'
        
        # Perform OCR
        text = pytesseract.image_to_string(processed_image_pil, config=custom_config)
        
        # Look for date pattern
        match = re.search(r'\d{2}\.\d{2}\.\d{4}', text)
        if match:
            date_str = match.group()
            date_obj = datetime.strptime(date_str, '%d.%m.%Y')
            return date_obj.date()
    except Exception:
        return None
    return None

def preprocess_image(image):
    """
    Preprocesses an image for OCR.

    Args:
        image (numpy.ndarray): The input image in OpenCV format.

    Returns:
        numpy.ndarray: The preprocessed image.
    """
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Increase contrast
    alpha = 2.0  # Simple contrast control
    beta = 0     # Simple brightness control
    contrast = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)
    
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(contrast, (5, 5), 0)
    
    # Apply thresholding
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    return thresh

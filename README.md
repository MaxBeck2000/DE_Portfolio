## Russian_Losses

**Russian_Losses** is a work-in-progress personal project designed to scrape documented Russian equipment losses in the Ukraine war from the webpage [Oryxspioenkop](https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html). The project aims to:

- **Scrape Data**: Extract information on Russian losses, including equipment type (e.g., tanks, aircraft), specific model (e.g., T-72), and links to confirming images or videos.
- **Database Storage**: Save the scraped data to a PostgreSQL database.
- **Visualizations**: Create visual representations of the losses throughout the war.

Additionally, there are plans to extend this project to include Ukrainian visually confirmed losses for comparison.

### Key Features

- **Data Extraction**: Captures detailed information about each loss entry, including:
  - **Equipment Type**: Categories like tanks, aircraft, etc.
  - **Specific Model**: For example, T-72.
  - **Image/Video Links**: URLs that confirm the loss.

- **Date Extraction**:
  - Some entries have readily available upload dates (e.g., from Twitter links).
  - Dates may also be found in image filenames.
  - For entries without easily accessible dates (approximately 40%), an Optical Character Recognition (OCR) program is being implemented.

### OCR Implementation

To address the challenge of missing dates, the project uses **Tesseract OCR** integrated into the main scraping script. The OCR program performs the following:

1. **Preprocessing Images**: Enhances image quality for better text recognition.
2. **Extracting Text**: Utilizes Tesseract to convert image content into text.
3. **Finding Dates**: Searches the extracted text for date patterns.

As of **01/08/2024**, the Tesseract-based script is operational and successfully extracts dates from images. Work is ongoing to process the thousands of images lacking easily accessible dates, aiming to minimize network strain while managing large-scale data.

### Future Plans

- **Extend to Ukrainian Losses**: Incorporate data on Ukrainian losses for comparative analysis.
- **Optimize Processing**: Continue improving the OCR processing to handle large volumes of images efficiently.

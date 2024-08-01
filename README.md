## Russian_Losses

**Russian_Losses** is a work-in-progress personal project designed to scrape documented Russian equipment losses in the Ukraine war from the webpage [Oryx](https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html). The project aims to:

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

### Folder Directory

- **Example Processed Images**: Contains a few examples of images before and after processing to enable more accurate transcription using Tesseract.
- **Test_Scripts**: Several rough scripts used to test some of the features in the project, such as testing connection to Postgres database, and finding dates from Twitter and other URLs.
- **find_date.py**: WIP script to work through the URLs from main_scrape that don't have an easy to find date. Uses Tesseract - need to implement a batch system still etc.
- **image_date.csv**: CSV file containing the URL and dates of images extracted using find_date.py, currently only populated with test image URL.
- **imgur.py**: WIP function to call from main_scrape, will find upload date of images in HTML. Currently only 2 images in DB use imgur, so not a priority.
- **main_scrape.py**: The main script to carry out the extraction, transformation, and loading of data from the Oryx webpage to the SQLite DB.
- **postimg.py**: Function that extracts the date of post from the postimg links that contain the date in the URL. Called from main_scrape.
- **russian_loss_data.db**: SQLite DB containing the scraped and transformed data.
- **twitter.py**: Function that extracts the upload date of tweets using the URL. Called from main_scrape.
- **urls_without_dates.csv**: CSV file containing all the image links that do not have an easily accessible date. Will be used in find_date.py to extract as many dates as possible.

## Basic_Data_Scrapes

- First few basic data scraping scripts for Fantasy Premier League dates and the retrieval of highly rated holiday destinations.

## Indian_Tolls_Scrape

- ETL tutorial project to extract details of the thousands of road toll booths in India.
- Loaded data to SQLite DB, which was then queried using DBeaver.

## Bootcamp Python

- Python learning materials from my Data Engineering bootcamp at my previous role.
  - **NLP**: Natural Language Processing code, including Generative AI and classification.
  - **Python**: Large variety of Python tutorials and questions, ranging from basic to data scraping, use of Pandas, programming, and virtual environments.
  - **Python Mock 1 & 2**: Past Python exams used for revision for my exam (100% attained).

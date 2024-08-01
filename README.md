Russian_Losses is a work in progress personal project to scrape the documented Russian losses of equipment in the Ukraine war from
the webpage https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html, save the data to a postgres database,
and produce visualisations of the losses throughout the war. I would also like to do this for the Ukrainian visually confirmed losses,
for comparison.
Each loss entry has data such as the type of equipment (e.g. tanks, aircraft, etc), the specific model (e.g. T-72), and a link to
the image/video that confirms the loss. Some entries have upload dates readily available - for example the twitter links contain the 
upload time and date in the URL. Others have dates saved in the image filename. Around 40%, however, don't have easily accessible 
dates, so I am in the process of implementing an Optical Character Recognition program to search for date stamps within the image.
To do this I am using Tesseract OCR along with my main scraping script. As of today (01/08/2024), the tesseract script is able to 
find dates in images, and I am working on an implementation for the thousands of images without easily accessible dates to be processed,
without putting too much strain on my network.

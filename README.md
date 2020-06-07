# GrubMenuScraper
A web scraper for collecting menu data from restaurant websites 

# Methodology

1. Obtain a list of keywords related to food from recipe websites (e.g. `['tomato', 'broccoli']`)
2. Scrape restaurant websites to obtain all DOM elements and associated text (e.g. `['<a href="???">Outback steakhouse</a>','<h3>Clam chowder</h3>', '<h3>Whopper</h3>']`)
3. Apply the list of keywords to scraped text and automatically find similarities in DOM structures for the detected menu items, therefore obtaining the best selector rule (e.g. `'body > div > div > h3'`)
4. Use the selector rule to precisely extract menu text (e.g. `['Clam chowder', 'Whopper']`)

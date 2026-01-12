PROJECT OVERVIEW:

    This is a webscraper that scrapes data from a webpage in two diffrent ways:
        -1: Using Regex
        -2: Using beautiful soup

    both of these scraping methods scrape for table elements:
    (<table>, <thead>, <tbody>, <tfoot>, <tr>, <th>, <td>) 
    from the population by country webpage, and then stores them in a default dictionary with position based keys

 FILES:

    -regexclass.py: Has the RegexExtraction class
    -beautifulsoupclass.py: Has the BeautifulSoupExtractor class
    -main.py: This is the main file that runs both of the scrapers

 Requirements:
    -Python 3
    -BeautifulSoup4 Library

 Installations needed:
    -run this in the terimnal:
        -pip install beautifulsoup4

How to Run/test:
    -execute in terminal:
        -python3 main.py

Format of Output:
    Data is stored with keys in the format: {tag}_{table_index}_{row_index}_{column_index}
    Example: td_1_5_3 = the 4th cell in the 6th row of the 2nd table

    
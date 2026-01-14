PROJECT OVERVIEW:

    This is a webscraper that scrapes HTML table data  from ANY user-provided url webpage in two diffrent ways:
        -1: Using Regex
        -2: Using beautiful soup

    While this scraper is capable of scraping HTML table data from any user provided URL,
    it was specifically built and tested for extraction of the:
                                        (<table>, <thead>, <tbody>, <tfoot>, <tr>, <th>, <td>) 
             elements from the Worldometers Population by Country webpage.

 FILE STRUCTURE:

    -main.py:
        This handles the commandline arguments, gets the URL and initializes the correct parser based off of user request.
    -abstract_class.py:
        This file contains the AbstractParser, a base class that defines shared logic between both parsers, with the display_data() and 
        store_data() methods.
    -regexclass.py:
        Contains the RegexExtraction class, which uses parsing logic with the python RE module.
    -beautifulsoupclass.py:
        Contains the BeautifulSoupExtactor class which uses parsing logic with bs4

 Requirements and Installation:
    To have sucess in running this program, you will need Python3 and a few external Python libraries.
        1: Please open your terminal and run the command below to install the required libraries:
                "pip install beautifulsoup4 pandas requests"

How to Run/test:
    This program gets run from the command line, and requires the user to input two arguments:
        - "--url": the target URL/website listed on the assingment sheet:  "https://www.worldometers.info/world-population/population-by-country/"
                                                                            (though it will work for ANY other user-provided url webpage)
        - "--parser": The type of parser that you want to use (regex or bs4)
    
    Examples of how to scrape
        using BeautifulSoup:
            In terminal:
                    python main.py --url "https://www.worldometers.info/world-population/population-by-country/" --parser bs4
        using Regex:
            In terminal:
                    python main.py --url "https://www.worldometers.info/world-population/population-by-country/" --parser regex
        An example of using the scraper with another website:
            In terminal:
                    python main.py --url "https://www.w3schools.com/html/html_tables.asp" --parser bs4

ISSUES/TROUBLESHOOTING:
    -If you get a message, such as "Sorry, but the url could not be fetched," please double check your internet connection is working
        and make sure that the URL is including: http:// or https://.
    -If the parser can't find the data, the website that you have inputed may not have the standard HTML <table> tags.

Format of Output:
    -The output prints the data scraped from the inputed site to the console. The data is stored in a dictionary where the Key represents the location of that data,
        and the value is the text content.

        Key Format: {tag}_{table_index}_{row_index}_{column_index}

    -Output Examples:
        table_1: Content of the first table found.

        tr_1_5: Content of the 5th row in the 1st table.

        td_1_5_3: Content of the 3rd cell (column) in the 5th row of the 1st table.

GOODBYE_MESSAGE:
    - Thanks for reading me! Have fun scraping :D !

    
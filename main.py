import argparse
import requests
import sys

from regexclass import RegexExtraction
from beautifulsoupclass import BeautifulSoupExtractor
# This will set up the command line used for the argument parser.
the_parser = argparse.ArgumentParser(
    description= "This will take the desired HTML table elements using either regex or BeautifulSoup"
)
#Defining for the required commandline args.
the_parser.add_argument("--url",  help="URL of the webpage to scrape")
the_parser.add_argument("--parser",help="Parser to use: 'regex' or 'bs4'" )
#Parse the arguments that are fed into the commandline.
the_args = the_parser.parse_args()
#extraction of URL from users arg.
url = the_args.url

headers = {"User-Agent": "Mozilla/5.0"}
#This makes an attempt at getting the webpage.
try:
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8' 
    html_text = response.text

except requests.RequestException:
    print("Sorry, but the url could not be fetched. To try and fix this error try checking the URL and also make sure you have a strong internet connection. Sorry for the inconvcience!")
    sys.exit(1)

    
#Validation for the parser that the user decides to use.
if the_args.parser not in ["regex", "bs4"]:
    print("This is not an available parser, sorry!")
    sys.exit(1)

#run the specefic parser that the user wants to use for websraping.
if the_args.parser == "regex":
    print("Regex Extraction:")
    regex_scraper = RegexExtraction(html_text)
    regex_scraper.display_data()
elif the_args.parser == "bs4":
    print("Beautiful Soup Exraction:")
    bs_scraper = BeautifulSoupExtractor(html_text)
    bs_scraper.display_data()



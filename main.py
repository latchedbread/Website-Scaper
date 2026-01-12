from regexclass import RegexExtraction
from beautifulsoupclass import BeautifulSoupExtractor
import requests

url = "https://www.worldometers.info/world-population/population-by-country/"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
html_text = response.text

print("Regex Extraction:")
regex_scraper = RegexExtraction(html_text)
regex_scraper.store_data()
regex_scraper.display_data()

print("Beautiful Soup Exraction:")
bs_scraper = BeautifulSoupExtractor(html_text)
bs_scraper.store_data()
bs_scraper.display_data()
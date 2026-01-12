from bs4 import BeautifulSoup
import requests
from collections import defaultdict
url = "https://www.worldometers.info/world-population/population-by-country/"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
html_text = response.text

class BeautifulSoupExtractor:

    def __init__(self, html_text):
        self.html_text = html_text
        self._defaultdict = defaultdict(list)
        self._tag_match_list = []
    
    def data_extraction(self):
        desired_tags = ["table", "thead", "tbody", "tfoot", "tr", "th", "td"]
        soup = BeautifulSoup(self.html_text, 'html.parser')
        for tag in desired_tags:
            tags_found = soup.find_all(tag)
            self._tag_match_list.extend(tags_found)
            

    def data_parsing(self):
        table_index = 0
        row_index = 0
        column_index = 0

        for match in self._tag_match_list:
            
            if match.name == "table":
                table_index += 1
                row_index = 0
                text_match = match.get_text()
                key = f"table_{table_index}"
                self._defaultdict[key] = text_match

            elif match.name == "thead":
                text_match = match.get_text()
                key = f"thead_{table_index}_{row_index}"
                self._defaultdict[key] = text_match

            elif match.name == "tbody":
                text_match = match.get_text()
                key = f"tbody_{table_index}_{row_index}"
                self._defaultdict[key] = text_match

            elif match.name == "tfoot":
                text_match = match.get_text()
                key = f"tfoot_{table_index}_{row_index}"
                self._defaultdict[key] = text_match

            elif match.name == "tr":
                row_index += 1
                column_index = 0
                text_match = match.get_text()
                key = f"tr_{table_index}_{row_index}"
                self._defaultdict[key] = text_match

            elif match.name == "td" or match.name == "th":
                column_index += 1
                text_match = match.get_text()
                key = f"{match.name}_{table_index}_{row_index}_{column_index}"
                self._defaultdict[key] = text_match

                

            

                

    def store_data(self):
        self.data_extraction()
        self.data_parsing()

    def display_data(self):
        for item in self._defaultdict:
            print(f"Data:{item}: {self._defaultdict[item]}")


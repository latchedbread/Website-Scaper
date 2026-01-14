from bs4 import BeautifulSoup
import pandas as pd
import requests
from collections import defaultdict
from abstract_class import AbstractParser



class BeautifulSoupExtractor(AbstractParser):

    """
    HTML table parser that uses the BeautifulSoup library.
    
    It extracts the desired elements : (table, thead, tbody, tfoot, tr, th, td)
    using BeautifulSoups parsing functions/capablities and stores them with structure
    """

    def __init__(self, html_text: str) -> None:
        """
        Initalizes the parser, and takes a string argument of the desired HTML content.
        """

        self.html_text = html_text
        self._defaultdict = defaultdict(list)
        self._tag_match_list = []
       #calling these methods insures that the HTML is extracted and parsed when the objects get instantiated.
        self.data_extraction()
        self.data_parsing()
    
    def data_extraction(self) -> list: #this method returns a list of tag objects
        """
        Extracts all the desired table tags: table, thead, tbody, tfoot, tr, th, and td
        using BeautifulSoup.

        Uses the find_all method to find all instances of the desired tags in the HTML.
        """

        desired_tags = ["table", "thead", "tbody", "tfoot", "tr", "th", "td"]
        soup = BeautifulSoup(self.html_text, 'html.parser')
        self._tag_match_list = soup.find_all(desired_tags)
        #makes sure that we have SOME tags
        if not self._tag_match_list:
                raise ValueError("No tags were found in the HTML that you provided!")
                 

    def data_parsing(self) -> pd.DataFrame: #returns a pandas data frame
        """
        Parses the already extracted tags.

        Processes them, and then gives them keys based on their type of tag and their position using:(table_index, row_index, column_index).
        """
        # Initialize at -1 so the first increment moves it to 0
        table_index = -1
        row_index = -1
        column_index = -1

        for match in self._tag_match_list:
            #table tag
            if match.name == "table":
                table_index += 1
                row_index = -1
                text_match = match.get_text().strip()
                key = f"table_{table_index}"
                self._defaultdict[key] = text_match
            #table header
            elif match.name == "thead":
                text_match = match.get_text().strip()
                key = f"thead_{table_index}_{row_index}"
                self._defaultdict[key] = text_match
            #table body
            elif match.name == "tbody":
                text_match = match.get_text().strip()
                key = f"tbody_{table_index}_{row_index}"
                self._defaultdict[key] = text_match
            #table footer
            elif match.name == "tfoot":
                text_match = match.get_text().strip()
                key = f"tfoot_{table_index}_{row_index}"
                self._defaultdict[key] = text_match
            #table row
            elif match.name == "tr":
                row_index += 1
                column_index = -1
                text_match = match.get_text().strip()
                key = f"tr_{table_index}_{row_index}"
                self._defaultdict[key] = text_match
            #table data/header cells
            elif match.name == "td" or match.name == "th":
                column_index += 1
                text_match = match.get_text().strip()
                key = f"{match.name}_{table_index}_{row_index}_{column_index}"
                self._defaultdict[key] = text_match

        if not self._tag_match_list:
            raise ValueError("The data was not able to be parsed from the tags!")
            #validation 

        try:
            data_frame = pd.DataFrame(list(self._defaultdict.items()), columns=['Key', 'Value'])
            return data_frame
            #Returns: pandas DataFrame with 'Key' and 'Value' columns 
        except Exception as e:
            raise ValueError(f"An error occured when trying to create the data frame: {e}")


            

                

    


import re
import requests
from collections import defaultdict
url = "https://www.worldometers.info/world-population/population-by-country/"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
html_text = response.text

class RegexExtraction:
    
    def __init__(self, html_text):
        self.html_text = html_text
        self._defaultdict = defaultdict(list)
        self._tag_match_list = []
        

    #this gets the data from the html_text
    def data_extraction(self):
        
        desired_tags = ["table", "thead", "tbody", "tfoot", "tr", "th", "td"]
        for tag in desired_tags:
            
            desired_pattern = rf"<{tag}[^>]*>(.*?)</{tag}>"
            
            text_match = re.findall(desired_pattern, self.html_text, re.DOTALL | re.IGNORECASE)

            self._tag_match_list.extend(text_match)
        
        print(f"Found {len(self._tag_match_list)} matches")  
        return self._tag_match_list
        
        


        

    
    def data_parsing(self):
        
        table_index = 0
        row_index = 0
        column_index = 0
        
        for tag in self._tag_match_list:
            print(f"Processing tag: {tag[:100]}")  # Print first 100 chars of each tag
            
            if "table" in tag:
                table_index += 1
                row_index = 0
                pattern = rf"<table.*?>(.*?)</table>"
                match = re.search(pattern, tag)
                if match:
                    text_content = match.group(1)
                    key = f"table_{table_index}"
                    self._defaultdict[key] = text_content
                
            
            elif "thead" in tag :
                pattern = rf"<thead.*?>(.*?)</thead>"
                match = re.search(pattern, tag)
                if match:
                    text_content = match.group(1)
                    key = f"thead_{table_index}_{row_index}"
                    self._defaultdict[key] = text_content

            elif "tbody" in tag:
                pattern = rf"<tbody.*?>(.*?)</tbody>"
                match = re.search(pattern, tag)
                if match:
                    text_content = match.group(1)
                    key = f"tbody_{table_index}_{row_index}"
                    self._defaultdict[key] = text_content
           
            elif "tfoot" in tag:
                pattern = rf"<tfoot.*?>(.*?)</tfoot>"
                match = re.search(pattern, tag)
                if match:
                    text_content = match.group(1)
                    key = f"tfoot_{table_index}_{row_index}"
                    self._defaultdict[key] = text_content
           
            elif "tr" in tag:
                row_index += 1
                column_index = 0
                pattern = rf"<tr.*?>(.*?)</tr>"
                match = re.search(pattern, tag)
                if match:
                    text_content = match.group(1)
                    key = f"tr_{table_index}_{row_index}"
                    self._defaultdict[key] = text_content
                    
            
            elif "td" in tag or "th" in tag:
                column_index += 1
                if "td" in tag:
                    pattern = r"<td.*?>(.*?)</td>"
                else:
                    pattern = r"<th.*?>(.*?)</th>"
                match = re.search(pattern, tag)
                if match:
                    text_content = match.group(1)
                    key = f"td_{table_index}_{row_index}_{column_index}"
                    self._defaultdict[key] = text_content


           
            


    

    
    def store_data(self):
        self.data_extraction()
        self.data_parsing()


    
    def display_data(self):
        for item in self._defaultdict:
            print(f"Data:{item}: {self._defaultdict[item]}")
        
        

    


  
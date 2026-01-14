import re
import pandas as pd
import requests
from collections import defaultdict
from abstract_class import AbstractParser


class RegexExtraction(AbstractParser):
    """
    This is and HTML parser that implements regex.

    It extracts the desired elements : (table, thead, tbody, tfoot, tr, th, td)
    using regex patterns and stores them with structure.
    """


    def __init__(self, html_text: str) -> None:
        """
        initalizes the parser, and takes a string argument of the desired HTML content.
        """


        self.html_text = html_text
        self._defaultdict = defaultdict(list)
        self._tag_match_list = []
        
        #calling these methods insures that the HTML is extracted and parsed when the objects get instantiated.
        self.data_extraction()
        self.data_parsing()

        

    #this gets the data from the html_text
    def data_extraction(self) -> list:

        """
        Looks for all instances of the desired html tags and stores their contents.
        This method returns a list whith the matching desired tag contents
        """
        
        # We extract the TABLES first. 
        # This is necessary because regex cannot handle nested tags (tr inside table) 
        # in a single pass without "swallowing" the inner tags.
        table_pattern = r"<table[^>]*>(.*?)</table>"
        self._tag_match_list = re.findall(table_pattern, self.html_text, re.DOTALL | re.IGNORECASE)

        if not self._tag_match_list:
            raise ValueError("No tags were found in the HTML that you provided!")
            #if no HTML tags are found 
        
          
        return self._tag_match_list
        
        


        

    
    def data_parsing(self) -> pd.DataFrame:

        """
        This method actually parses the tags that we have extracted.
        Assigns the tags unique keys based on the type of tag and their position
        (table_index, row_index, column_index).
        """
        # Initialize at -1 so the first increment moves it to 0
        table_index = -1
        row_index = -1
        column_index = -1
        
        # Iterate through the tables we extracted in step 1
        for table_content in self._tag_match_list:
            table_index += 1
            row_index = -1   # Reset row count for new table
            
            # Cleaning table content (remove tags)
            clean_table_content = re.sub(r'<[^>]+>', '', table_content).strip()
            key = f"table_{table_index}"
            self._defaultdict[key] = clean_table_content

            # 1. OPTIONAL: Capture headers/body/footers inside this table
            for section in ["thead", "tbody", "tfoot"]:
                section_pattern = rf"<{section}[^>]*>(.*?)</{section}>"
                sections = re.findall(section_pattern, table_content, re.DOTALL | re.IGNORECASE)
                for sec_idx, sec_content in enumerate(sections):
                    clean_sec = re.sub(r'<[^>]+>', '', sec_content).strip()
                    self._defaultdict[f"{section}_{table_index}_{sec_idx}"] = clean_sec

            # 2. FIND ROWS: Look inside the current table content for <tr> tags
            row_pattern = r"<tr[^>]*>(.*?)</tr>"
            rows = re.findall(row_pattern, table_content, re.DOTALL | re.IGNORECASE)

            for row_content in rows:
                row_index += 1
                column_index = -1 # Reset column count for new row
                
                # Cleaning row content
                clean_row = re.sub(r'<[^>]+>', '', row_content).strip()
                key = f"tr_{table_index}_{row_index}"
                self._defaultdict[key] = clean_row

                # 3. FIND CELLS: Look inside the current row content for <td> or <th> tags
                # Group 1 = tag name, Group 2 = content
                cell_pattern = r"<(td|th)[^>]*>(.*?)</\1>"
                cells = re.findall(cell_pattern, row_content, re.DOTALL | re.IGNORECASE)

                for tag_name, cell_content in cells:
                    column_index += 1
                    
                    # --- FIX START ---
                    # 1. Remove all HTML tags (like <a href...>) from inside the cell
                    clean_text = re.sub(r'<[^>]+>', '', cell_content)
                    # 2. Strip whitespace
                    clean_text = clean_text.strip()
                    # --- FIX END ---

                    # Store cell content
                    key = f"{tag_name}_{table_index}_{row_index}_{column_index}"
                    self._defaultdict[key] = clean_text

        #error handling that makes sure that the parsing gave the results
        if not self._defaultdict:
            raise ValueError("The data was not able to be parsed from the tags!") 

        #coverts to DataFrame to make our output more structured than phase 1's output
        try:
            data_frame = pd.DataFrame(list(self._defaultdict.items()), columns=['Key', 'Value'])
            return data_frame 
        except Exception as e:
            raise ValueError(f"An error occured when trying to create the data frame: {e}")
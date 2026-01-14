from abc import ABC, abstractmethod

class AbstractParser(ABC):

    """
    This is an abstract class that both the regex and the beautifulsoup parser can use
   
    There's a commonality between both classes for storing and displaying the data from the table after its been parsed.
    Subclasses have their own seperate logic for the data_extraction and data_parsing methods
    
    """
    def store_data(self) -> None:

        """
        Calls the data_extraction and the data_parsing methods, is it be inherited by both regex and beautiful soup class
        
        """



        self.data_extraction()
        self.data_parsing()

    def display_data(self) -> None:
        """
        This method prints all of the finished and correctly parsed data to the console.
        display_data iterates through the default dic and disaplys the keyval pair in an easy, readable format for the user

        """


        for item in self._defaultdict:
            print(f"Data:{item}: {self._defaultdict[item]}")

    

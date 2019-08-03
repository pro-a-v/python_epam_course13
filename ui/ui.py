from abc import ABC, abstractmethod
import logging

class UI(ABC):
    """
    Virtual class for UI interface
    """
    def __init__(self):
        logging.basicConfig(filename="./data/tagcounter.log", level=logging.INFO)

    def get_url(self, tag: str) -> str:
        """ method to transfer tag into url

        Parameters
        ----------
        tag : str
            The tag that used for query
        """
        print("Drew a chess piece")

    def get(self, url: str) -> dict:
        """ method to query result from provided url

        Parameters
        ----------
        url: str
        The url that used for query
        """
        pass

    @abstractmethod
    def show(self):
        # abstract method - depends on interface - to show the results
        pass
from abc import ABC, abstractmethod

class Storage(ABC):
    """
    Virtual class for Storage interface
    """

    @abstractmethod
    def get(self, url: str) -> str:
        """ method to get data from db

        Parameters
        ----------
        url : str
            The url that used for query table
        """
        pass

    @abstractmethod
    def save(self, pickle_data: dict):
        """ method to save data to db

        Parameters
        ----------
        pickle_data: dict
            dict with keys url-URL and  tag-count
        """
        pass


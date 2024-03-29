from abc import ABC, abstractmethod, ABCMeta

class _Storage(ABC):
    """
    Virtual class for Storage interface
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get(self, url: str) -> dict:
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



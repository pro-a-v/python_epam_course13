from abc import ABC, abstractmethod, ABCMeta

class _HttpClient(ABC):
    """
    Virtual class for Storage interface
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get(self, url: str) -> str:
        """ method to request data from remote side and return str response

        Parameters
        ----------
        url : str
            The url that used for query
        """

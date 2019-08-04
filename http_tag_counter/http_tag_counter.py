from abc import ABC, abstractmethod, ABCMeta

class _HttpTagCounter(ABC):
    """
    Virtual class for Storage interface
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def process(self, data: str) -> dict:
        """ method to calculate tag count in provided string (http content)

        Parameters
        ----------
        data : str
            Http raw data represented in string
        """

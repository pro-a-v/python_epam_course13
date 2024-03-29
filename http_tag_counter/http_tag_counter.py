from abc import ABC, abstractmethod, ABCMeta
from collections import defaultdict

class _HttpTagCounter(ABC):
    """
    Virtual class for Storage interface
    """
    __metaclass__ = ABCMeta
    def __init__(self):
        self.occurrences = defaultdict(int)

    @abstractmethod
    def process(self, data: str) -> dict:
        """ method to calculate tag count in provided string (http content)

        Parameters
        ----------
        data : str
            Http raw data represented in string
        """

    def inc_tag(self, tag: str):
        self.occurrences[tag] += 1

    def get(self):
        return self.occurrences
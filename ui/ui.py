from abc import ABC, abstractmethod, ABCMeta
import logging

from storage.storage_sqlalchemy_sqlite import Storage
from http_client.httpclient_requests import HttpClient
from http_tag_counter.http_tag_counter_loader import HttpTagCounter
from synonyms.synonyms_loader import synonyms_loader

class UI(ABC):
    """
    Virtual class for UI interface
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        logging.basicConfig(filename="tagcounter.log",
                            level=logging.INFO,
                            format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',)


        self.result = dict()

    def get_url(self, tag: str) -> str:
        """ method to transfer tag into url

        Parameters
        ----------
        tag : str
            The tag that used for query
        """
        print("Drew a chess piece")

    def get(self, url: str) -> dict:
        """ method to query from www result from provided url

        Parameters
        ----------
        url: str
        The url that used for query
        """
        html = HttpClient().get(url=url)
        tags = HttpTagCounter().load(type='HTMLParser').process(html)
        self.result['url'] = url
        self.result['data'] = tags
        storage = Storage()
        storage.save(self.result)

        #tags = HttpTagCounter().load(type='beautifulsoup').process(html)
        #tags = HttpTagCounter().load(type='lxml').process(html)


    def view(self, url: str) -> dict:
        """ method to query from DB result from provided url

        Parameters
        ----------
        url: str
        The url that used for query
        """
        storage = Storage()
        self.result = storage.get(url)

    @abstractmethod
    def show(self):
        """
        abstract method - depends on interface - to show the results
        """



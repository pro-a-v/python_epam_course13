from http_tag_counter.http_tag_counter import _HttpTagCounter
from bs4 import BeautifulSoup



class HttpTagCounter(_HttpTagCounter):
    def __init__(self):
        super.__init__()
        pass


    def get(self, data: str) -> dict:
        soup = BeautifulSoup(data)
        for tag in soup.findAll():
            print(tag.name)
        return None
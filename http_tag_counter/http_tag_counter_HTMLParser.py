from HTMLParser import HTMLParser
from http_tag_counter.http_tag_counter import _HttpTagCounter


class HttpTagCounter(_HttpTagCounter, HTMLParser):
    def __init__(self):
        _HttpTagCounter.__init__(self)
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        self.inc_tag(tag)

    def process(self, data: str) -> dict:
        self.feed(data)
        return self.get()

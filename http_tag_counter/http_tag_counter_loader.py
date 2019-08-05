import importlib

class HttpTagCounter():
    def load(self, type = 'beautifulsoup'):
        if type == 'beautifulsoup':
            module = importlib.import_module('http_tag_counter.http_tag_counter_beautifulsoup')
            my_class = getattr(module, 'HttpTagCounter')
            return my_class()
        if type == 'HTMLParser':
            module = importlib.import_module('http_tag_counter.http_tag_counter_HTMLParser')
            my_class = getattr(module, 'HttpTagCounter')
            return my_class()
        if type == 'lxml':
            module = importlib.import_module('http_tag_counter.http_tag_counter_lxml')
            my_class = getattr(module, 'HttpTagCounter')
            return my_class()

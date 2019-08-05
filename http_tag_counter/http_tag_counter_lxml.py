from http_tag_counter.http_tag_counter import _HttpTagCounter
import lxml.etree
import io

class HttpTagCounter(_HttpTagCounter):
    def __init__(self):
        super().__init__()
        pass


    def process(self, data: str) -> dict:
        root = lxml.etree.HTML(data)
        #for tag in root.findAll():
        #    self.inc_tag(tag.name)

        context = lxml.etree.iterwalk(root, events=("start", ))
        for action, elem in context:
            self.inc_tag(elem.tag)

        return self.get()
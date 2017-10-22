import cStringIO as StringIO
import pprint

class ParsleyItemClassLoader(object):
    def __init__(self, item_class, item_loader_class, parselet, item_key, response, **context):
        self.item_class = item_class
        self.item_loader_class = item_loader_class
        self.parselet = parselet
        self.item_key = item_key
        self.response = response

    def iter_items(self):
        self.extracted = self.parselet.parse(StringIO.StringIO(self.response.body))
        for item_value in self.extracted.get(self.item_key):
            loader = self.item_loader_class(self.item_class())
            loader.add_value(None, item_value)
            yield loader.load_item()

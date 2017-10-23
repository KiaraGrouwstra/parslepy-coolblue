import cStringIO
# import pprint
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class MyItemLoader(ItemLoader):
    '''scrapy item loader'''
    default_output_processor = TakeFirst()

def iter_parsley(item_cls, parselet, response, item_key):
    loader = MyItemLoader(item_cls())
    data = parselet.parse(cStringIO.StringIO(response.body))
    if item_key:
        for item_value in data.get(item_key):
            loader.add_value(None, item_value)
            yield loader.load_item()
    else:
        loader.add_value(None, data)
        yield loader.load_item()

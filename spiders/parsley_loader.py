import cStringIO
# import pprint
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class MyItemLoader(ItemLoader):
    '''
    my default scrapy item loader, takes the first item found
    '''
    default_output_processor = TakeFirst()

def iter_parsley(item_cls, parselet, response):
    loader = MyItemLoader(item_cls())
    for item_value in parselet.parse(cStringIO.StringIO(response.body)).get('items'):
        loader.add_value(None, item_value)
        yield loader.load_item()

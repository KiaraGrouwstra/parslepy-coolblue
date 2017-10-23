'''parsley spider'''
import cStringIO
import json
import yaml
from scrapy import Spider
from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from parslepy import Parselet

class MyItemLoader(ItemLoader):
    '''scrapy item loader'''
    default_output_processor = TakeFirst()

def get_item_class(props):
    '''get an item class for the given keys'''
    class ItemCls(Item):
        '''item class with dynamic properties'''
        fields = {k : Field() for k in props}
    cls = ItemCls()
    for k in props:
        cls._values[k] = Field()
    return cls

class ParsleySpider(Spider):
    '''scrape a parselet'''
    name = 'Parsley'
    allowed_domains = ['nytimes.com']
    start_urls = ['http://www.nytimes.com/pages/technology/']
    item_cls = get_item_class(['title', 'author', 'summary', 'image', 'url', 'timestamp'])

    def __init__(self, **kwargs):
        super(ParsleySpider, self).__init__(**kwargs)
        self.item_key = kwargs['item_key']
        self.parselet = Parselet.from_jsonstring(json.dumps(yaml.load(kwargs['parselet'])))

    def parse(self, response):
        loader = MyItemLoader(self.item_cls)
        data = self.parselet.parse(cStringIO.StringIO(response.body))
        if self.item_key:
            for item_value in data.get(self.item_key):
                loader.add_value(None, item_value)
                yield loader.load_item()
        else:
            loader.add_value(None, data)
            yield loader.load_item()

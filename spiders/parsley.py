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

def parselet_keys(parselet):
    '''get the item keys from a parselet dict'''
    keys = parselet.keys()
    if keys[0][-1] == ')':
        return parselet_keys(parselet.values()[0])
    else:
        return keys

class ParsleySpider(Spider):
    '''scrape a parselet'''
    name = 'Parsley'

    def __init__(self, **kwargs):
        super(ParsleySpider, self).__init__(**kwargs)
        self.item_key = kwargs['item_key']
        dic = yaml.load(kwargs['parselet'])
        self.parselet = Parselet.from_jsonstring(json.dumps(dic))
        keys = ['title', 'author', 'summary', 'image', 'url', 'timestamp']
        # keys = parselet_keys(dic)
        self.item_cls = get_item_class(keys)
        domain = kwargs['domain']
        self.allowed_domains = [domain]
        url = kwargs.get('url', 'https://{}/'.format(domain))
        self.start_urls = [url]

    def parse(self, response):
        # self.logger.debug('crawled url {}'.format(response.request.url))
        loader = MyItemLoader(self.item_cls)
        data = self.parselet.parse(cStringIO.StringIO(response.body))
        if self.item_key:
            for item_value in data.get(self.item_key):
                loader.add_value(None, item_value)
                yield loader.load_item()
        else:
            loader.add_value(None, data)
            yield loader.load_item()
        # for link in scrapy.linkextractors.lxmlhtml.LxmlParserLinkExtractor().extract_links(response):
        #     yield scrapy.http.Request(link.url, callback=self.parse)
        # yield vars(response)
        # #patts = item['attrs']['dump_patterns']
        # #if (not patts) or (patts and (regex.search(response.request.url) for regex in patts)):
        # #    yield item

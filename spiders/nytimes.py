'''
scrape NYTimes
'''
# import pprint
import json
import yaml
import scrapy
import parslepy
from spiders.parsley_loader import ParsleyItemClassLoader
from spiders.nytimes_news_item import NYTimesNewsItem
from spiders.nytimes_loader import NYTimesItemLoader

class NYTimesSpider(scrapy.Spider):
    '''
    scrape NYTimes
    '''
    name = 'NYTimes'
    allowed_domains = ['nytimes.com']
    start_urls = ['http://www.nytimes.com/pages/technology/']

    def __init__(self, **kwargs): # , *args
        if kwargs['parselet']:
            parselet = json.dumps(yaml.load(kwargs['parselet']))
            self.parselet = parslepy.Parselet.from_jsonstring(parselet) # from_jsonfile(open(path))
        super(NYTimesSpider, self).__init__() # (*args, **kwargs)

    def parse(self, response):
        loader = ParsleyItemClassLoader(NYTimesNewsItem, NYTimesItemLoader, self.parselet, item_key="newsitems", response=response)
        return loader.iter_items()

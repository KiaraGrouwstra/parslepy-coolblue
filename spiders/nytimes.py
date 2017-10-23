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

    def __init__(self, **kwargs):
        super(NYTimesSpider, self).__init__(**kwargs)
        parselet = json.dumps(yaml.load(kwargs['parselet']))
        self.parselet = parslepy.Parselet.from_jsonstring(parselet)

    def parse(self, response):
        return ParsleyItemClassLoader(NYTimesNewsItem, NYTimesItemLoader, self.parselet, item_key="newsitems", response=response).iter_items()

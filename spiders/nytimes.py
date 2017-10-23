'''scrape NYTimes'''
# import pprint
import json
import yaml
import scrapy
from parslepy import Parselet
from spiders.parsley_loader import iter_parsley
from spiders.nytimes_news_item import NYTimesNewsItem

class NYTimesSpider(scrapy.Spider):
    '''scrape NYTimes'''
    name = 'NYTimes'
    allowed_domains = ['nytimes.com']
    start_urls = ['http://www.nytimes.com/pages/technology/']

    def __init__(self, **kwargs):
        super(NYTimesSpider, self).__init__(**kwargs)
        self.item_key = kwargs['item_key']
        self.parselet = Parselet.from_jsonstring(json.dumps(yaml.load(kwargs['parselet'])))

    def parse(self, response):
        return iter_parsley(NYTimesNewsItem, self.parselet, response, self.item_key)

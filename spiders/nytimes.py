'''scrape NYTimes'''
import json
import yaml
import scrapy
from parslepy import Parselet
from spiders.parsley_loader import iter_parsley
from spiders.nytimes_news_item import NYTimesNewsItem, get_item_class

class NYTimesSpider(scrapy.Spider):
    '''scrape NYTimes'''
    name = 'NYTimes'
    allowed_domains = ['nytimes.com']
    start_urls = ['http://www.nytimes.com/pages/technology/']
    item_cls = NYTimesNewsItem()
    # item_cls = get_item_class(['title', 'author', 'summary', 'image', 'url', 'timestamp'])

    def __init__(self, **kwargs):
        super(NYTimesSpider, self).__init__(**kwargs)
        self.item_key = kwargs['item_key']
        self.parselet = Parselet.from_jsonstring(json.dumps(yaml.load(kwargs['parselet'])))

    def parse(self, response):
        return iter_parsley(self.item_cls, self.parselet, response, self.item_key)

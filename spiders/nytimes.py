# import cStringIO as StringIO
import pprint
import scrapy
import parslepy
import json
# import spiders
import parsley_loader
import nytimes_news_item
import nytimes_loader

class NYTimesSpider(scrapy.Spider):
    name = 'NYTimes'
    allowed_domains = ['nytimes.com']
    start_urls = ['http://www.nytimes.com/pages/technology/']

    def __init__(self, *args, **kwargs):
    # def __init__(self, parseletfile=None):
        # if parseletfile:
        #     with open(parseletfile) as jsonfp:
        #         self.parselet = parslepy.Parselet.from_jsonfile(jsonfp)
        # pprint.pprint("kwargs")
        # pprint.pprint(kwargs)
        # if kwargs['parseletfile']:
        #     with open(kwargs['parseletfile']) as jsonfp:
        #         pprint.pprint("jsonfp")
        #         pprint.pprint(jsonfp)
        #         self.parselet = parslepy.Parselet.from_jsonfile(jsonfp)
        #         pprint.pprint("self.parselet")
        #         pprint.pprint(self.parselet)
        #         pprint.pprint("self.parselet.parselet")
        #         pprint.pprint(self.parselet.parselet)
        if kwargs['parselet']:
            self.parselet = parslepy.Parselet.from_jsonstring(kwargs['parselet'])
        super(NYTimesSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        parselet = parslepy.Parselet.from_jsonstring(self.parselet)
        # extracted = self.parselet.parse(StringIO.StringIO(response.body))
        loader = parsley_loader.ParsleyItemClassLoader(
            nytimes_news_item.NYTimesNewsItem,
            nytimes_loader.NYTimesItemLoader,
            # self.parselet,
            parselet,
            item_key="newsitems",
            response=response)
        return loader.iter_items()

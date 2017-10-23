'''parsley spider'''
from cStringIO import StringIO
from re import search
from json import dumps as json_dumps
from yaml import load as yaml_load
from scrapy import Spider
from scrapy.http import Request
from scrapy.linkextractors.lxmlhtml import LxmlParserLinkExtractor
from parslepy import Parselet

class ParsleySpider(Spider):
    '''scrape a parselet
        *domain:    the domain to crawl
        url:        seed url, default domain index
        *parselet:  path to the yaml file
        crawl:      whether to crawl, default False
        pattern:    regex of urls to dump, default all crawled
    '''
    name = 'Parsley'

    def __init__(self, **kwargs):
        with open(kwargs['parselet']) as _f:
            yml = _f.read()
        dic = yaml_load(yml)
        domain = kwargs['domain']
        url = kwargs.get('url', 'https://{}/'.format(domain))
        super(ParsleySpider, self).__init__(**kwargs)
        self.crawl = bool(kwargs.get('crawl', 0))
        self.pattern = kwargs.get('pattern', '')
        self.parselet = Parselet.from_jsonstring(json_dumps(dic))
        self.allowed_domains = [domain]
        self.start_urls = [url]

    def parse(self, response):
        if search(self.pattern, response.request.url):
            # yield vars(response)
            data = self.parselet.parse(StringIO(response.body))
            if len(data.keys()) == 1 and isinstance(data.values()[0], list):
                for item_value in data.values()[0]:
                    yield item_value
            else:
                yield data
        else:
            self.logger.debug('skip url {}'.format(response.request.url))

        if self.crawl:
            for link in LxmlParserLinkExtractor().extract_links(response):
                yield Request(link.url, callback=self.parse)

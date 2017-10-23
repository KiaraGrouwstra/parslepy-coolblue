'''parsley spider'''
import cStringIO
import json
import yaml
from scrapy import Spider
from parslepy import Parselet

class ParsleySpider(Spider):
    '''scrape a parselet'''
    name = 'Parsley'

    def __init__(self, **kwargs):
        with open(kwargs['parselet']) as _f:
            yml = _f.read()
        dic = yaml.load(yml)
        domain = kwargs['domain']
        url = kwargs.get('url', 'https://{}/'.format(domain))
        super(ParsleySpider, self).__init__(**kwargs)
        self.parselet = Parselet.from_jsonstring(json.dumps(dic))
        self.allowed_domains = [domain]
        self.start_urls = [url]

    def parse(self, response):
        # self.logger.debug('crawled url {}'.format(response.request.url))
        data = self.parselet.parse(cStringIO.StringIO(response.body))
        if len(data.keys()) == 1 and isinstance(data.values()[0], list):
            for item_value in data.values()[0]:
                yield item_value
        else:
            yield data
        # for link in scrapy.linkextractors.lxmlhtml.LxmlParserLinkExtractor().extract_links(response):
        #     yield scrapy.http.Request(link.url, callback=self.parse)
        # yield vars(response)
        # #patts = item['attrs']['dump_patterns']
        # #if (not patts) or (patts and (regex.search(response.request.url) for regex in patts)):
        # #    yield item

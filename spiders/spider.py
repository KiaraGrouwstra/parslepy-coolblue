"""base spider"""
import re
from scrapy import Spider
from scrapy.http import Request
from scrapy.linkextractors.lxmlhtml import LxmlParserLinkExtractor

class MySpider(Spider):
    """ Crawl and spider
        *domain:    the domain to crawl
        url:        seed url, default domain index
        crawl:      whether to crawl, default False
        pattern:    regex of urls to dump, default all crawled
    """
    name = 'My'

    def __init__(self, **kwargs):
        domain = kwargs['domain']
        url = kwargs.get('url', 'https://{}/'.format(domain))
        super(MySpider, self).__init__(**kwargs)
        self.crawl = bool(kwargs.get('crawl', 0))
        self.pattern = kwargs.get('pattern', '')
        self.allowed_domains = [domain]
        self.start_urls = [url]

    def parse(self, response):
        url = response.request.url
        if re.search(self.pattern, url):
            for data in self.process(response):
                yield data
        else:
            self.logger.debug('skip url {}'.format(url))
        if self.crawl:
            for link in LxmlParserLinkExtractor().extract_links(response):
                yield Request(link.url, callback=self.parse)

    def process(self, response):
        yield vars(response)

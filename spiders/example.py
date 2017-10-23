import scrapy
# from scrapy.http import Request
# from scrapy.spiders import Spider
# from scrapy.linkextractors.lxmlhtml import LxmlParserLinkExtractor

class LinkSpider(scrapy.spiders.Spider):
    name = 'link'
    allowed_domains = ['www.coolblue.nl']
    start_urls = ['https://www.coolblue.nl/']

    # def __init__(self, *args, **kwargs):
    #     super(LinkSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        self.logger.debug('crawled url {}'.format(response.request.url))
        for link in scrapy.linkextractors.lxmlhtml.LxmlParserLinkExtractor().extract_links(response):
            yield scrapy.http.Request(link.url, callback=self.parse)
        yield vars(response)
        #patts = item['attrs']['dump_patterns']
        #if (not patts) or (patts and (regex.search(response.request.url) for regex in patts)):
        #    yield item

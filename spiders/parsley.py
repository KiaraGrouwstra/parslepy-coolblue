"""parsley spider"""
from cStringIO import StringIO
from extruct import extract as extruct
from spiders.spider import MySpider
from parslepy import Parselet

class ParsleySpider(MySpider):
    """ Scrape a parselet
        *parselet:  path to the yaml file
    """
    name = 'Parsley'

    def __init__(self, **kwargs):
        with open(kwargs['parselet']) as _f:
            parselet = Parselet.from_yamlfile(_f)
        super(ParsleySpider, self).__init__(**kwargs)
        self.parselet = parselet

    def process(self, response):
        """ extract with parselet"""
        body = response.body
        data = self.parselet.parse(StringIO(body))
        if len(data.keys()) == 1 and isinstance(data.values()[0], list):
            for item_value in data.values()[0]:
                yield item_value
        else:
            data.update(extruct(body, response.request.url))
            yield data

"""kafka spider"""
from __future__ import absolute_import
import json
from extruct import extract as extruct
from spiders.spider import MySpider
from toolz.curried import merge, pipe
from fp import pick, evolve
from kafka import KafkaProducer

class KafkaSpider(MySpider):
    """ Scrape to kafka"""
    name = 'Kafka'

    def __init__(self, **kwargs):
        super(KafkaSpider, self).__init__(**kwargs)
        val_ser = lambda v: json.dumps(v).encode('utf-8')
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=val_ser)

    def process(self, response):
        """ send to Kafka"""
        data = \
            merge(extruct(response.body), \
            evolve({'request': vars}, \
            pick(['status', 'request', '_body', '_url', 'headers'], \
            vars(response))))
        self.producer.send(self.pattern, data)
        yield data

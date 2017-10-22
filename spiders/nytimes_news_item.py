from scrapy.item import Item, Field
from scrapy.loader.processors import TakeFirst

class NYTimesNewsItem(Item):
    title = Field(output_processor=TakeFirst())
    author = Field(output_processor=TakeFirst())
    summary = Field()
    image = Field()
    url = Field()
    timestamp = Field()

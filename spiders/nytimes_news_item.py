'''item schema'''
from scrapy.item import Item, Field

class NYTimesNewsItem(Item):
    '''NYTimes news item'''
    title = Field()
    author = Field()
    summary = Field()
    image = Field()
    url = Field()
    timestamp = Field()

def get_item_class(props):
    '''get an item class for the given keys'''
    class ItemCls(Item):
        '''item class with dynamic properties'''
        fields = {}
    cls = ItemCls()
    cls['fields'] = {k : Field() for k in props}
    for k in props:
        # setattr(cls, k, Field())
        cls[k] = Field()
    return cls

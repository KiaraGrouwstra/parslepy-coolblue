'''item schema'''
from scrapy.item import Item, Field

def get_item_class(props):
    '''get an item class for the given keys'''
    class ItemCls(Item):
        '''item class with dynamic properties'''
        fields = {k : Field() for k in props}
    cls = ItemCls()
    for k in props:
        cls._values[k] = Field()
    return cls

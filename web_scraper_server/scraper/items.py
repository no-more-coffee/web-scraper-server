from scrapy.item import Field, Item


class ApartmentItem(Item):
    id = Field()
    title = Field()
    image = Field()

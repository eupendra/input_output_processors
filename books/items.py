# # Define here the models for your scraped items
# #
# # See documentation in:
# # https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from price_parser import Price
from w3lib.html import remove_tags


def get_price(p):
    price_object = Price.fromstring(p)
    return price_object.amount_float


def get_availability(p: list):
    for data in p:
        if 'In Stock' in data:
            return True
    return False


class BooksItem(scrapy.Item):
    title = scrapy.Field(
        output_processor=TakeFirst()
    )
    price = scrapy.Field(
        input_processor=MapCompose(get_price),
        output_processor=TakeFirst()
    )
    available = scrapy.Field(
        output_processor=get_availability
    )


# class BooksItem(scrapy.Item):
#     title = scrapy.Field()
#     price = scrapy.Field()
#     available = scrapy.Field()

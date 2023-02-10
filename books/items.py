# # Define here the models for your scraped items
# #
# # See documentation in:
# # https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from price_parser import Price
from w3lib.html import remove_tags


def get_price_in(p):
    price_object = Price.fromstring(p)
    return price_object.amount_float


def get_currency_in(p):
    price_object = Price.fromstring(p)
    currency = price_object.currency
    return currency


def get_availability_out(p:list):
    for data in p:
        if 'In Stock' in data:
            return True
    return False


class BooksItem(scrapy.Item):
    title = scrapy.Field(
        output_processor=TakeFirst()  # calling method
    )
    price = scrapy.Field(
        input_processor=MapCompose(get_price_in),
        output_processor=TakeFirst()  # calling method
    )
    available = scrapy.Field(
        output_processor=get_availability_out  # calling method
    )

    currency = scrapy.Field(
        input_processor=MapCompose(get_currency_in),
        output_processor=TakeFirst()  # calling method
    )
    
# Plain Item
# class BooksItem(scrapy.Item):
#     title = scrapy.Field()
#     price = scrapy.Field()
#     currency = scrapy.Field()
#     available = scrapy.Field()
#     currency = scrapy.Field()

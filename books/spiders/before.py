import scrapy
from books.items import BooksItem
from price_parser import Price

def get_price(p):
    price_object = Price.fromstring(p)
    return price_object.amount_float

def get_availability(p:list):
    for data in p:
        if 'In Stock' in data:
            return True
    return False

class BeforeSpider(scrapy.Spider):
    name = 'before'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        for book in response.css('ol.row li'):
            price = get_price(book.css('.price_color::text').get())
            available = get_availability(book.css('.instock::text').getall())


            item = dict()
            item['title'] = book.css('img::attr(alt)').get()
            item['available'] = available
            item['price'] = price
            yield item

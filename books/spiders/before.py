import scrapy
from price_parser import Price
from books.items import BooksItem

class BeforeSpider(scrapy.Spider):
    name = 'before'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        for book in response.css('ol.row li'):
            price_raw = book.css('.price_color::text').get()
            price_object = Price.fromstring(price_raw)

            # available?
            available = False
            for data in book.css('.instock::text').getall():
                if 'In Stock' in data:
                    available = True
                    continue

            item = dict()
            item['title'] = book.css('img::attr(alt)').get()
            item['available'] = available
            item['price'] = price_object.amount_float
            item['currency'] = price_object.currency
            print(item)

import scrapy
from itemloaders import ItemLoader

from books.items import BooksItem


class AfterSpider(scrapy.Spider):
    name = 'after'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        for book in response.css('ol.row li'):
            l = ItemLoader(item=BooksItem(), selector=book)

            l.add_css('title', 'img::attr(alt)')
            l.add_css('available', '.instock::text')
            l.add_css('price', '.price_color::text')
            l.add_css('currency', '.price_color::text')

            yield l.load_item()

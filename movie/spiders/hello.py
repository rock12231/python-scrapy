import scrapy

class QuotesSpider(scrapy.Spider):
    name = "main"
    start_urls = ['https://coold.in']

    def parse(self, response):
        title = response.css('title::text').extract()
        yield {'titletext': title}
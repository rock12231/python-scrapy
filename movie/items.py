# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from turtle import title
import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    # start_urls = ['https://coold.in']
    
    # def parse(self, response):
    #     title = response.css('title::text').extract()
    #     yield {'titletext': title}
    pass
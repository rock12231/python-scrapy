import json
from pkg_resources import yield_lines
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "main"
    start_urls = ['https://www.justwatch.com/ag/movie/k-g-f-chapter-1']

    def parse(self, response):
        # title = response.css('div.detail-infos__value::text').extract()
        Genre = response.css('div.detail-infos__value::text').extract()
        Director_Name = response.css('div.detail-infos__value::text').extract()
        # Cast = response.css('div.cast::text').extract()
        # Release_year = response.css('div.year::text').extract()
        # Language = response.css('div.language::text').extract()
        # Duration = response.css('div.duration::text').extract()
        # IMDb_Ratings = response.css('div.imdb::text').extract()
        # Movie_name = response.css('div.name::text').extract()
        # Movie_Link = response.css('div.name a::attr(href)').extract()
        movie_json = {	
        "Genre" : Genre,
        "Director_Name" : Director_Name,
        # "Cast" : Cast,
        # "Release_year" : Release_year,
        # "Language" : Language,
        # "Duration"   : Duration,
        # "IMDb_Ratings" : IMDb_Ratings,
        # "Movie_name" : Movie_name,
        # "Movie_Link" : Movie_Link
        }
        with open('data.json', 'w') as f:     
            json.dump(movie_json, f)
        # yield {'title' : title}
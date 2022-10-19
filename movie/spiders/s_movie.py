import json
import scrapy

class QuotesSpider(scrapy.Spider):
    # Name of spider
    name = "main"
    # URLs to crawl
    start_urls = ['https://www.justwatch.com/ag/movie/k-g-f-chapter-1']

    def parse(self, response):
        # Get Data
        Genre = response.css('div.detail-infos__value span::text').getall()
        Director_Name = response.css('div.detail-infos__value span a::text').get()
        Cast = response.css('div.hidden-horizontal-scrollbar__items .title-credits__actor a::text').extract()
        Release_year = response.css('div.title-block div span::text').get()
        # Language = response.css('div.language::text').extract()
        Duration = response.css('div.detail-infos__value::text').get()
        IMDb_Ratings = response.css('div.jw-scoring-listing__rating a::text').extract()
        Movie_name = response.css('div.title-block div h1::text').get()
        Movie_Link = response.request.url
        
        # Filter Data
        val = ", "
        Genre = [i for i in Genre if i != val]
        Release_year = Release_year.replace("(","")
        Release_year = Release_year.replace(")","")
        
        # Create Dictionary
        movie_json = {	
        "Genre" : Genre,
        "Director_Name" : Director_Name,
        "Cast" : Cast,
        "Release_year" : Release_year,
        # "Language" : Language,
        "Duration"   : Duration,
        "IMDb_Ratings" : IMDb_Ratings,
        "Movie_name" : Movie_name,
        "Movie_Link" : Movie_Link
        }
        
        # Convert to data.JSON file
        with open('data.json', 'w') as f:     
            json.dump(movie_json, f)
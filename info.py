import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd

# imort list of urls
links = pd.read_csv('url.csv')
player_list = list(links)


# open file to store info
f2 = open('info.csv', 'w+') 


class FIFA_spider_info(scrapy.Spider):
    name = 'FIFA_spider_info'

    allowed_domains = ['www.fifaindex.com']
    start_urls = player_list

    def parse(self, response):
        # extract info for each player
	    # EDIT over here to get more info
        player = response.css('h1::text').extract_first()
        measure = response.css('div.card-body>p:nth-of-type(1)>*> span.data-units::text').extract_first()
        

	# Write info to file
	# If you collect more info, make changes here also
        f2.write(str(player))
        f2.write(',')
        f2.write(str(measure))
        f2.write('\n')


process2 = CrawlerProcess()
process2.crawl(FIFA_spider_info)
process2.start()

f2.close()

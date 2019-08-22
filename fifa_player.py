# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess

player_list = []


class FIFA_spider(scrapy.Spider):
    name = 'FIFA_spider'

    allowed_domains = ['www.fifaindex.com']
    start_urls = ['https://www.fifaindex.com/players/fifa20/']

    def parse(self, response):
        links = response.css('a.link-player::attr(href)')

        for players in links:
            rel_link = players.extract()
            player_url = 'https://www.fifaindex.com' + rel_link  # link to players page
            player_list.append(player_url)

        if (response.css('ul.pagination').xpath('./li//text()').extract_first() == 'Next Page'):
            new_page = response.css('ul.pagination').xpath('./li').css('a.btn::attr(href)').extract_first()
            # print('RUN DONE')
            if new_page is not None:
                url = 'https://www.fifaindex.com' + new_page
                yield scrapy.Request(url, callback=self.parse_page1)


    def parse_page1(self, response):
        links = response.css('a.link-player::attr(href)')

        for players in links:
            rel_link = players.extract()
            player_url = 'https://www.fifaindex.com' + rel_link  # link to players page
            player_list.append(player_url)

        if (response.css('ul.pagination').xpath('./li//text()').extract_first() == 'Previous Page'):
            new_page = response.css('ul.pagination').xpath('./li[2]').css('a.btn::attr(href)').extract_first()
            # print('RUN DONE')
            if new_page is not None:
                url = 'https://www.fifaindex.com' + new_page
                yield scrapy.Request(url, callback=self.parse_page1)


process = CrawlerProcess()
process.crawl(FIFA_spider)
process.start()

# write the players urls to a file
f = open('url.csv', 'w+')
for player in player_list:
    f.write(str(player))
    f.write(',')
f.close()

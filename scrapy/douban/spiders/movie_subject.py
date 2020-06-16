# -*- coding: utf-8 -*-
import scrapy
from douban.items import Subject

class MovieSubjectSpider(scrapy.Spider):
    name = 'movie_subject'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for movie in movie_list:
            douban_item = Subject()
            url_subject = movie.xpath("./div[@class='item']/div[@class='info']//a/@href").get()
            douban_item['douban_id'] = url_subject.split('subject/')[1][:-1]           
            douban_item['movie_name'] = movie.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").get()
            douban_item['star'] = movie.xpath(".//span[@class='rating_num']/text()").get()
            douban_item['description'] = movie.xpath(".//p[@class='quote']/span/text()").get()
            yield douban_item
        next_link = response.xpath("//span[@class='next']/link/@href").get()
        if next_link:
            yield scrapy.Request("https://movie.douban.com/top250"+next_link, callback=self.parse)
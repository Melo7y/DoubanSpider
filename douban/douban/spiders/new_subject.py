# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import redis

class NewSubjectSpider(CrawlSpider):
    name = 'new_subject'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/25785556']
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    rules = (
        Rule(LinkExtractor(allow=r'movie.douban.com/subject/\d+/\?from'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        #item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        print(response.url)
        subject_id = response.url.split("subject")[1].split("/")[1]
        self.r.sadd("subject_id", subject_id)

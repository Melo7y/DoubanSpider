# -*- coding: utf-8 -*-
import scrapy
import douban.database as db
from douban.items import Comment
cursor = db.connection.cursor()

class MovieCommentSpider(scrapy.Spider):
    name = 'movie_comment'
    allowed_domains = ['movie.douban.com']
    
    '''
    sql = "SELECT douban_id FROM movies where douban_id not in (\
        select douban_id, count(*) num from comments GROUP BY douban_id) a where a.num > 1\
        )"
    '''

    sql = "SELECT douban_id FROM subjects"
    cursor.execute(sql)
    subjects = cursor.fetchall()

    start_urls = [
        'https://movie.douban.com/subject/%s/comments?status=P' % subject for subject in subjects 
    ]



    def parse(self, response):
        response_url = response.url
        if 404 == response.status:
            print("404 Not Found, url:", response_url)
        else:
            douban_id = response_url.split("subject")[1].split("/")[1]

            item_regx = '//div[@class="mod-bd"]/div[@class="comment-item"]'
            comment_item_list = response.xpath(item_regx)

            for comment_item in comment_item_list:
                comment = Comment()
                print("executing respective comment...", comment_item)
                #user_regx = '/div[@class="comment"]//span[@class="comment-info"]'
                username = comment_item.xpath('.//div[@class="comment"]//span[@class="comment-info"]/a/text()').get()
                rating = comment_item.xpath('.//div[@class="comment"]//span[@class="comment-info"]/span[contains(@class, "allstar")]/@title').get()
                content = comment_item.xpath('.//div[@class="comment"]/p/span[@class="short"]/text()').get()
                comment_time = comment_item.xpath('.//div[@class="comment"]//span[@class="comment-info"]/span[contains(@class,"comment-time")]/@title').get()
                comment_id = comment_item.xpath('.//@data-cid').get()
                
                comment['douban_id'] = douban_id
                comment['douban_username'] = username
                comment['rating'] = rating
                comment['content'] = content
                comment['comment_time'] = comment_time
                comment['douban_comment_id'] = comment_id
                yield comment

            next_url = response.xpath('//a[@class="next"]/@href').get()
            if next_url:
                url = "https://movie.douban.com/subject/%s/comments%s" %(douban_id, next_url)
                yield scrapy.Request(url, callback=self.parse)
 

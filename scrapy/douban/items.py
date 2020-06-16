# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class Subject(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    douban_id = Field()
    movie_name = Field()
    star = Field()
    description = Field()


class Comment(Item):
    douban_id = Field()
    douban_comment_id = Field()
    douban_username = Field()
    content = Field()
    rating = Field()
    comment_time = Field()


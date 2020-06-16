# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from douban.items import Subject, Comment
import douban.database as db

class DoubanPipeline():
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(host=crawler.settings.get("MYSQL_HOST"),
                   database=crawler.settings.get("MYSQL_DATABASE"),
                   user=crawler.settings.get("MYSQL_USER"),
                   password=crawler.settings.get("MYSQL_PASSWORD"),
                   port=crawler.settings.get("MYSQL_PORT"))

    def open_spider(self, spider):

        self.cursor = db.connection.cursor()

    def close_spider(self, spider):
        db.connection.close()

    def get_subject(self, item):
        if item["douban_id"] == '':
            print("Get Subject Exception: douban_id id null")

        sql = 'SELECT id FROM subjects WHERE douban_id=%s' % item['douban_id']
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    def get_comment(self, item):
        sql = 'SELECT * FROM comments WHERE douban_comment_id = %s' % item['douban_comment_id']
        self.cursor.execute(sql)
        return self.cursor.fetchone()
        
    def save_comment(self, item):
        keys = item.keys()
        values = tuple(item.values())
        fields = ','.join(keys)
        temp = ','.join(['%s'] * len(keys))
        sql = 'INSERT INTO comments (%s) VALUES (%s)' % (fields, temp)
        self.cursor.execute(sql, values)
        return db.connection.commit()

    def save_subject(self, item):
        if item["douban_id"] == '':
            print("Save Subject Exception: douban_id is null")
        else:
            keys = item.keys()
            values = tuple(item.values())
            fields = ','.join(keys)
            temp = ','.join(['%s'] * len(keys))
            sql = 'INSERT INTO subjects (%s) VALUES (%s)' % (fields, temp)
            self.cursor.execute(sql, values)
            return db.connection.commit()

    def process_item(self, item, spider):
        if isinstance(item, Subject):
            exist = self.get_subject(item)
            if not exist:
                self.save_subject(item)       
        elif isinstance(item, Comment):

            exist = self.get_comment(item)
            if not exist:
                try:
                    self.save_comment(item)
                except Exception as e:
                    print(item)
                    print(e)


        return item

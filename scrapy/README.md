# Scrapy项目文件结构介绍

本爬虫基于Scrapy框架，各目录和文件的功能介绍说明如下：

1. douban

   i.  spiders：存放爬虫文件，也就是重点需要自己实现的部分

   * movie_subject.py ------------ 爬取电影的douban_id
   * movie_comment.py ---------电影评论的爬取

   ii. douban/items.py ------ 用来定义项目实体，格式比较像字典，爬虫获取的信息会放在实体中，进入管道。

   iii. douban/middlewares.py --------定义下载器中间件和爬虫中间件

   iv. douban/pipelines.py --------- 定义Item Pipeline的实现，主要功能包括数据清洗，验证和存储。

   v. douban/settings.py ---------- 全局配置

   vi. douban/util.py ------------- 工具类文件

   vii. douban/database.py 数据库的配置和连接

2. db.sql ------- MySQL脚本文件，可以执行

3. scrapy.cfg -------------配置文件

# 请求头中添加cookie

本项目中重写了start_requests方法，在请求头的cookie中随机生成了bid，查阅了网上相关内容，据说可以减少封禁的风险。


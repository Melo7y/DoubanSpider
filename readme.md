# Douban Spider（豆瓣影评爬虫）

此项目是本人的本科毕业设计，主要针对豆瓣电影的的评论进行爬取。爬虫项目采用了Scrapy框架，并且采用了代理，爬取评论的速度非常快。代理有免费和付费之分，免费的代理肯定不太好用，建议采用付费代理，几十块钱可以满足大多数人的需求。如果爬取数据量较小，也可不适用代理。

# 安装说明

首先需要安装Python3，版本最好>= 3.6

1. Clone代码

   `git clone git@github.com:AIAIAIAIAI/DoubanSpider.git`

2. 安装MySQL数据库

   将scrapy目录下的db.sql脚本文件执行，创建好相关的表，然后配置好scrapy/douban/database.py中的数据库用户名和密码

3. 如果需要使用代理池，会用到Redis数据库，Redis数据库的安装，请自行搜索

4. 安装Python相关依赖库

   `pip install -r requirements.txt`

5. 执行爬取程序，详细见douban目录下README

**注意：因为添加了代理池，每次代理之前，代理池会从Redis数据库中获取代理IP，如果不使用代理，在settings.py文件中的DOWNLOADER_MIDDLEWARES中ProxyMiddleware注释掉即可（添加#，如下）**

```python
DOWNLOADER_MIDDLEWARES = {
  #'douban.middlewares.ProxyMiddleware': 543,
  'douban.middlewares.RandomUserAgentMiddleware': 544,
}
```

# 使用示例

然后对电影数据进行爬取，命令如下：

```
# 进入scrapy目录
cd scrapy
# 查看爬虫列表
scrapy list
# 爬取subject，主要是电影相关信息以及douban_id
scrapy crawl movie_subject
# 接着根据douban_id爬取评论
scrapy crawl movie_comment
```

下图是本人使用代理单机爬取两小时的结果：



![38a94ea1dde740b6889e9cbb9a727c8](C:\Users\Melo\Documents\DoubanSpider\img\38a94ea1dde740b6889e9cbb9a727c8.png)
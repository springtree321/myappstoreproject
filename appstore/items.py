# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

#   cd appstore
#   scrapy crawl huawei

class HuaweiAppstoreItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    appid = scrapy.Field()
    intro = scrapy.Field()
    recommended = scrapy.Field()
    thumbnailURL = scrapy.Field()



class XiaomiAppstoreItem(scrapy.Item):
    title = scrapy.Field()
    appid = scrapy.Field()
    recommended = scrapy.Field()



class ScrapyWebItem(Item):
    Heading = Field()
    Content = Field()
    Url = Field()



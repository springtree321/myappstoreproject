#!/usr/bin/python
#-*-coding:utf-8-*-
import random

from scrapy import log
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware

class RandomProxyMiddleware(HttpProxyMiddleware):
    def __init__(self, proxy='Scrapy'):
        self.proxy = proxy

    def process_request(self, request, spider):
        proxy = random.choice(self.proxy_list)
        if proxy:
            print "------Current Proxy:%s ------" %proxy
            request.headers.setdefault('Proxy', proxy)

    proxy_list = [
        "218.104.69.106",
        "115.29.37.249",
        "123.126.32.102",
        "117.135.250.133",
        "124.126.126.105",
        "218.104.69.106",
        "123.126.32.102",
        "107.151.152.221",
        "92.46.125.177",
        "50.30.152.130",
        "85.194.242.10",
        "117.135.250.133",
        "185.5.64.70",
        "201.217.55.164",
    ]
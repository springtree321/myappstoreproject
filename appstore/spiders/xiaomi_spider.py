import scrapy
import re
from scrapy.spiders import Spider
from scrapy import Request
from scrapy.selector import Selector
from appstore.items import XiaomiAppstoreItem

class XiaomiSpider(Spider):
    name = "xiaomi"
    allowed_domains = ["app.mi.com"]
    start_urls = ["http://app.mi.com/topList?page=1"]
    
    def parse(self, response):
        page = Selector(response)
        page_nexts = page.xpath('//div[@class="pages"]/a')
        page_max = int(page_nexts[-2].xpath('text()').extract_first())
        
        for page_id in xrange(1, 2):
            url = '{0}{1}'.format('http://app.mi.com/topList?page=', str(page_id))
            yield scrapy.Request(url, callback=self.parse_page)
        
    def parse_page(self, response):
        page = Selector(response)
        lis = page.xpath('//ul[@class="applist"]/li')
        if lis == None:
            return
        url_common = 'http://app.mi.com'
        for li in lis:
            item = XiaomiAppstoreItem()
            item['title'] = li.xpath('./h5/a/text()').extract_first().encode('utf-8')
            url = li.xpath('./h5/a/@href').extract_first()
            item['appid'] = re.match(r'/detail/(.*)', url).group(1)
            req = scrapy.Request(url_common + url, callback = self.parse_details)
            req.meta["item"] = item
            yield req
        
    def parse_details(self, response):
            item = response.meta["item"]
            page = Selector(response)
            lis = page.xpath('//div[@class="second-imgbox"]/ul/li')
            recommended = []
            for li in lis:
                url = li.xpath('./a/@href').extract_first()
                appid = re.match(r'/detail/(.*)', url).group(1)
                recommended.append(appid)
            item['recommended'] = recommended
            yield item
import scrapy
import re
from scrapy.selector import Selector
from appstore.items import HuaweiAppstoreItem

from scrapy.spiders import Spider
#from scrapy import Request
from appstore.items import ScrapyWebItem

class HuaweiSpider(Spider):
    name = "huawei"
    allowed_domains = ["huawei.com"]
    start_urls = ["http://appstore.huawei.com/more/all"]
    
    # def parse(self, response):
    #     page = Selector(response)
    #     divs = page.xpath('//div[@class="game-info  whole"]')
    #     #print("divs size: ", len(divs))
    #     for div in divs:
    #         item = AppstoreItem()
    #         item['title'] = div.xpath('.//h4[@class="title"]/a/text()').extract_first().encode('utf-8')
    #         item['url'] = div.xpath('.//h4[@class="title"]/a/@href').extract_first()
    #         item['intro'] = div.xpath('.//p[@class="content"]/text()').extract_first().encode('utf-8')
    #         item['appid'] = re.match(r'http://.*/(.*)', item['url']).group(1)
    #         #item['appid'] = item['url'].split('/')[-1]
    #         yield item
        
    def parse(self, response):
        page = Selector(response)
        hrefs = page.xpath('//h4[@class="title"]/a/@href')
        for href in hrefs:
            url = href.extract()
            yield scrapy.Request(url, callback=self.parse_item)
            
    def parse_item(self, response):
        page = Selector(response)
        item = HuaweiAppstoreItem()
        item['title'] = page.xpath('.//span[@class="title"]/text()').extract_first().encode('utf-8')
        item['url'] = response.url
        item['appid'] = re.match(r'http://.*/(.*)', item['url']).group(1)
        item['intro'] = page.xpath('.//meta[@name="description"]/@content').extract_first().encode('utf-8')
        item['thumbnailURL'] = page.xpath('.//img[@class="app-ico"]/@lazyload').extract_first()
        divs = page.xpath('//div[@class="open-info"]')
        recomm = ""
        for div in divs:
            url = div.xpath('./p[@class="name"]/a/@href').extract_first()
            recommended_appid = re.match(r'http://.*/(.*)', url).group(1)
            name = div.xpath('./p[@class="name"]/a/text()').extract_first().encode('utf-8')
            recomm += "{0}:{1},".format(recommended_appid, name)
        item['recommended'] = recomm
        yield item
            


class ScrapySpider(Spider):
    name = "Scrapy"
    allowed_domains = ["scrapy.org"]
    start_urls = ["http://scrapy.org/"]
    def parse(self, response):
        page = Selector(response)
        item = ScrapyWebItem()
        item['Heading'] = page.xpath('/html/body/div[2]/div/div[1]/div/div[1]/p[2]/text()').extract()
        item['Content'] = page.xpath('/html/body/div[2]/div/div[1]/div/div[1]/p[1]/text()').extract()
        item['Url'] = "http://scrapy.org/"
        return item
        
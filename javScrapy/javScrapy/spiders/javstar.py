import scrapy
import logging
from pandas import DataFrame
from datetime import date, timedelta
from scrapy import Request, FormRequest
from ..items import JavscrapyItem


class JavidSpider(scrapy.Spider):
    name = "javstar"
    allowed_domains = ["javbus.com"]
    start_urls = 'https://www.javbus.com/star/okq'

    def start_requests(self):
        url = 'https://www.javbus.com/star/okq'
        yield Request(url, callback=self.get_page)

    def get_page(self, response):
        page_num = response.xpath('//div[6]/ul/li/a').extract()
        total_page = len(page_num)-1
        for page in range(total_page):
            url = '{url}/{page}'.format(url=self.start_urls, page=(page + 1))
            yield FormRequest(url, callback=self.parse_index)

    ## 获取所有av
    def parse_index(self, response):
        avarray = []
        # 获取av链接
        av = response.xpath('//a[@class="movie-box"]/@href').extract()
        # 把所有av写入数组
        for link in av:
            avarray.append(link)
        for url in avarray:
            yield Request(url, callback=self.parse_magnet)

    def parse_magnet(self, response):
        # open(file='detail.html', mode='wb').write(response.body)
        magnet = response.xpath('//tr/td/a[contains(text(),"高清")]/ancestor::tr/td/a/@href').extract_first()
        # 发送至流水线模式
        # item = JavscrapyItem()
        # for field in item.fields:
        #    item[field] = eval(field)
        # yield item
        # 先清除临时文件再写入最新数据
        if magnet is not None:
            with open(str(date.today()) + ".magnet.txt", "a") as temp:
                temp.write(magnet + '\n')
        pass

    def parse(self, response):
        pass

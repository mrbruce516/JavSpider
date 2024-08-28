import scrapy
import logging
from pandas import DataFrame
from datetime import date, timedelta
from scrapy import Request, FormRequest
from ..items import JavscrapyItem


class JavidSpider(scrapy.Spider):
    name = "javid"
    allowed_domains = ["javbus.com"]
    start_urls = 'https://www.javbus.com/page'

    def start_requests(self):
        for page in range(5):
            url = '{url}/{page}'.format(url=self.start_urls, page=(page + 1))
            yield FormRequest(url, callback=self.parse_index)

    # 获取今天发售的最新AV
    def parse_index(self, response):
        today = str(date.today()+timedelta(days=-1))
        avdict = {}
        # 获取av发售日期
        avday = response.xpath('//div[@class="photo-info"]/span/date[2]/text()').extract()
        if today not in avday:
            logging.info('今日无新种，养生！')
        # 获取av链接
        av = response.xpath('//a[@class="movie-box"]/@href').extract()
        when = 0
        # 把av和对应的发售日期写入字典
        for create in av:
            avdict[create] = avday[when]
            when += 1
        # 获取当天的av，用pd筛选后写入list
        data = DataFrame([avdict.keys(), avdict.values()]).T
        data.rename(columns={0: 'site', 1: 'day'}, inplace=True)
        selectav = data.where(data['day'] == today).dropna(axis=0, how='all')
        avlist = selectav['site'].values.tolist()
        for url in avlist:
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

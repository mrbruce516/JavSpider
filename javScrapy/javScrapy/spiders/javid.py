import scrapy
from datetime import date
from scrapy import Request, FormRequest
from ..items import JavscrapyItem


class JavidSpider(scrapy.Spider):
    name = "javid"
    allowed_domains = ["javbus.com"]
    start_urls = 'https://www.javbus.com/genre/sub'

    def start_requests(self):
        for page in range(1):
            url = '{url}/{page}'.format(url=self.start_urls, page=(page + 1))
            yield FormRequest(url, callback=self.parse_index)

    # 获取当前页所有av
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
        carid = response.xpath('//span[@style="color:#CC0000;"]/text()').extract_first()
        actor = response.xpath('//span[@class="genre"]/a/text()').extract_first()
        category_array = response.xpath('//span[@class="genre"]/label/a/text()').getall()
        category = ",".join(map(str, category_array))
        releaseDate = response.xpath('//div/p[2]/text()').extract_first()
        magnet = response.xpath('//tr[td/a[contains(text(),"高清")]][td/a[contains(text(),"字幕")]]/td/a/@href').extract_first()
        # 发送至流水线模式
        item = JavscrapyItem()
        for field in item.fields:
           item[field] = eval(field)
        yield item
        # 先清除临时文件再写入最新数据
        if magnet is not None:
            with open(str(date.today()) + ".magnet.txt", "a") as temp:
                temp.write(magnet + '\n')
        pass

    # TODO: 调用aria2下载，并且修改数据库状态为1

    def parse(self, response):
        pass

# main.py
import scrapy
from scrapy.crawler import CrawlerProcess
from javScrapy.write_magnet import write_magnet
from scrapy.utils.project import get_project_settings

# 获取项目设置
settings = get_project_settings()

# 创建 CrawlerProcess 实例
process = CrawlerProcess(settings)

# 定义爬虫列表
spiders = [
    'javid',
]

# 启动爬虫
for spider_name in spiders:
    process.crawl(spider_name)

# 开始爬虫
process.start()
write_magnet()

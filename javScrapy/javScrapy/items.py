# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JavscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    carid = scrapy.Field()
    actor = scrapy.Field()
    category = scrapy.Field()
    releaseDate = scrapy.Field()
    magnet = scrapy.Field()

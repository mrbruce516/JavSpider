# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from twisted.python.win32 import quoteArguments

from .database import DBConnection


class JavscrapyPipeline:
    def process_item(self, item, spider):
        # 写入文件 调试用
        with open("magnet.txt", "a") as file:
            # 因为item中的数据是unicode编码的，为了在控制台中查看数据的有效性和保存，将其编码改为utf-8
            item_string = str(item)
            file.write(item_string+'\n')
        # 写入数据库
        db = DBConnection(host='localhost')
        sql = "INSERT INTO javscrapy VALUES (UUID(), %s, %s, %s, %s, '0')"
        values = (item['carid'],item['actor'], item['category'], item['magnet'])
        db.execute(sql, values)
        db.disconnect()
        return item

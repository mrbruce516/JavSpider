# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class JavscrapyPipeline:
    def open_spider(self, spider):
        # 打开数据库连接
        self.connection = pymysql.connect(
            #host='db',
            host='localhost',
            user='root',
            password='scrapy',
            database='scrapy',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        # 关闭数据库连接
        self.connection.close()

    def process_item(self, item, spider):
        # 写入文件 调试用
        #with open("magnet.txt", "a") as file:
        #    # 因为item中的数据是unicode编码的，为了在控制台中查看数据的有效性和保存，将其编码改为utf-8
        #    item_string = str(item)
        #    file.write(item_string+'\n')
        # 写入数据库
        sql = "INSERT INTO javscrapy VALUES (UUID(), %s, %s, %s, %s)"
        values = (item['carid'],item['actor'], item['category'], item['magnet'])
        self.cursor.execute(sql, values)
        self.connection.commit()
        return item

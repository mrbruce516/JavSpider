# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging
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
        sql = "INSERT INTO javscrapy VALUES (UUID(), %s, %s, %s, %s, %s, '0')"
        values = (item['carid'], item['actor'], item['category'], item['releaseDate'], item['magnet'])
        check_sql = "SELECT * FROM javscrapy WHERE carid = %s"
        update_sql = "UPDATE javscrapy SET magnet = %s,status = 0 WHERE carid = %s"
        update_values = (item['magnet'], item['carid'])
        result = db.execute(check_sql, item['carid'])
        if not result:
            db.execute(sql, values)
            logging.debug("数据新增成功")
        elif result[0]['carid'] == item['carid'] and result[0]['magnet'] != item['magnet']:
            db.execute(update_sql, update_values)
            logging.debug("数据更新成功")
        else:
            logging.debug("数据已存在，跳过")
        db.disconnect()
        return item

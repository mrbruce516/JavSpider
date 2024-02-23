# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class JavscrapyPipeline:
    def process_item(self, item, spider):
        with open("magnet.txt", "a") as file:
            # 因为item中的数据是unicode编码的，为了在控制台中查看数据的有效性和保存，将其编码改为utf-8
            item_string = str(item)
            file.write(item_string+'\n')
        return item

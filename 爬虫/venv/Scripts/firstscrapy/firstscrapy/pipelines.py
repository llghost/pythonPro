# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class FirstscrapyPipeline(object):

    def __init__(self):
        print("========================init================")

    def process_item(self, item, spider):
        print("----------------------------process--------------",spider)
        self.file.write(json.dumps(dict(item)) + ',\n')
        return item

    def open_spider(self,spider):
        print(spider,'-----------------open----')
        print(spider.settings.get("filename"))
        self.file=open(spider.settings.get('filename'),'w',encoding='utf-8')
        self.file.write("[\n")

    def close_spider(self,spider):
        print(spider,'-----------------close----')
        self.file.write("]")
        self.file.close()

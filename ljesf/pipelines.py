# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import sqlite3

class LjesfPipeline(object):
    def open_spider(self, spider):
        self.con = sqlite3.connect("ljesf.sqlite")
        self.cu = self.con.cursor()

    def process_item(self, item, spider):
        print(spider.name,'pipelines')
        insert_sql = "insert into ljesf (title,info,region,totalprice,price) values('{}', '{}', '{}','{}', '{}')".format(item['title'], item['info'], item['region'], item['totalprice'], item['price'])
        print(insert_sql)
        self.cu.execute(insert_sql)
        self.con.commit()
        return item

    def spider_close(self, spider):
        self.con.close()

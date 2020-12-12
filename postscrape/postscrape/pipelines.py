# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class PostscrapePipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("myquotes.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_th""")
        self.curr.execute("""
        create table quotes_th
        (title text,
        date text,
        author text)""")

    def process_item(self, item, spider):
        self.store_db(item)

        return item

    def store_db(self, item):
        self.curr.execute("""insert into quotes_th values(?,?,?)""", (
            item['title'],
            item['date'],
            item['author']


        ))
        self.conn.commit()


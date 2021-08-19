# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class AmazontutoPipeline:
    def __init__(self):
        self.create_database()
        self.create_table()

    def create_database(self):
        self.conn = sqlite3.connect('amazon.db')
        self.curr = self.conn.cursor()
    
    def create_table(self):
        self.curr.execute('''DROP TABLE IF EXISTS mobile_phone_tb''')
        self.curr.execute('''CREATE TABLE mobile_phone_tb(phone TEXT, phone_brand TEXT, price TEXT, image_links TEXT)''')

    def store_db(self, item):
        phone_brand = item['phone_brand']
        phone = item['phone']
        price = item['price']
        image_links = item['image_links']

        self.curr.execute('''INSERT INTO mobile_phone_tb VALUES (?, ?, ?, ?)''',(phone, phone_brand, price, image_links))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

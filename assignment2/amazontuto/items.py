# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazontutoItem(scrapy.Item):
    # define the fields for your item here like:
    phone_brand = scrapy.Field()
    image_links = scrapy.Field()
    price = scrapy.Field()
    phone = scrapy.Field()
    

import scrapy
from ..items import AmazontutoItem


class SpyzonSpider(scrapy.Spider):
    name = 'spyzon'
    allowed_domains = ['amazon.in']
    start_urls = ['https://www.amazon.in/s?i=electronics&bbn=1389401031&rh=n%3A976419031%2Cn%3A1389401031%2Cn%3A1389432031%2Cp_89%3AApple&dc&qid=1629210538&rnid=1389401031&ref=sr_nr_n_2']

    def parse(self, response):
        items = AmazontutoItem()
        phones_details = response.xpath("//div[@class='sg-col-inner']/span/div")
        for phone in phones_details:
            phone_brand = response.xpath("//li//a//label/input[@type='checkbox' and @checked]/../../../span/text()").get(default='brand not selected')
            phone_name = phone.xpath(".//div[@class='a-section a-spacing-none']//h2//span/text()").get(default='Not given')
            price= phone.xpath(".//div[@class='a-section a-spacing-none a-spacing-top-small']//a/span[1]/span[@class='a-offscreen']/text()").get(default='Not given')
            image_links= phone.xpath(".//span[@class='rush-component']//div/img/@src").get(default='Not given')

            items['phone_brand'] = phone_brand
            items['phone'] = phone_name
            items['price'] = price
            items['image_links'] = image_links

            yield items 

        next_page = response.xpath("//a[contains(text(),'Next')]/@href").get()
        print(next_page)
        if next_page:
            yield scrapy.Request(url=f'https://www.amazon.in{next_page}', callback=self.parse)

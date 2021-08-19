import scrapy


class SpycoronaSpider(scrapy.Spider):
    
name = 'corona_data'
    
allowed_domains = ['worldometers.info']
    
start_urls = ['https://www.worldometers.info/coronavirus/']

    
def parse(self, response):
        
countries = response.xpath("//table[@id='main_table_countries_today']/tbody/tr[@style='' or contains(@style,'background-color')]")

        
for country in countries:yield{
"Country": country.xpath(".//td[2][@style='font-weight: bold; font-size:15px; text-align:left;']//text()")[0].extract(),
                
"Total Cases": country.xpath(".//td[3]/text()")[0].extract(),
                
"New Cases": country.xpath(".//td[4]/text()").get(default="0"),
                
"Total Deaths": country.xpath(".//td[5]/text()").get(default='0').strip(),
                
"Total Recovered": country.xpath(".//td[7]/text()").get(default='0').strip(),
                
"Active Cases": country.xpath(".//td[9]/text()").get(default='0').strip(),
  }

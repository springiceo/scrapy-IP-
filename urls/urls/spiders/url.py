import re
import scrapy
from urls.items import UrlsItem


class UrlSpider(scrapy.Spider):
    name = 'url'
    allowed_domains = ['51job.com']
    start_urls = ['http://51job.com/']
    item = UrlsItem()

    def parse(self, response):
        urls = [i.replace('//','') for i in response.xpath('//div[@id="area_channel_homepage_all"]/div/span/a/@href').getall()]
        for url in urls:
            yield scrapy.Request(url='https://'+url,callback=self.page_url)


    def page_url(self,response):
        city = response.xpath('//div[@class="e inter"]/div/a/@href').get()
        city_id = re.findall('list/(.*?),0000,',city)
        city_url = 'https://search.51job.com/list/'+city_id[0]+',0000,00,9,99,+,2,1.html'
        city_u = 'https://search.51job.com/list/'+city_id[0]+',0000,00,9,99,+,2,{}.html'
        yield scrapy.Request(url=city_url,callback=self.page_list,meta={'url':city_u})

    def page_list(self,response):
        page = re.findall('"total_page":"(.*?)"',response.text)[0]
        city_url = response.meta['url']
        for page in range(1,int(page)+1):
            url = city_url.format(page)
            self.item['url'] = url
            print(url)
            # yield self.item








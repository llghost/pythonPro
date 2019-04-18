# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
from ..items import FirstscrapyItem
#scrapy genspider -t basic book douban.com  模板生成命令
# scrapy  lits  爬虫列表
#scrapy crawl book 执行爬虫
#scrapy crawl book -o books.json 输出到文件 一般json  不支持.txt

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start=0&type=T']
    custom_settings = {
        'filename':'d:/doubanbook.json'
    }
    def parse(self, response:HtmlResponse):
        print("--------------------------------------------------")
        #items=[]
        subjects = response.xpath('//li[@class="subject-item"]')
        for subject in subjects:
            title = subject.xpath('.//h2/a/text()').extract()  # list
            # print(title[0].strip())
            rate = subject.xpath('.//span[@class="rating_nums"]/text()').extract()  # list
            # print(rate[0].strip())
            item = FirstscrapyItem()
            item['title'] = title[0].strip()
            item['rate'] = rate[0].strip()
            yield item
            #items.append(item)
        # print(type(response))
        # print(type(response.text),type(response.body))
        # with open("d:/douban.json","w",encoding="utf-8") as f:
        #     for item in items:
        #         f.write('{}:{}\n'.format(item['title'],item['rate']))
        # return items



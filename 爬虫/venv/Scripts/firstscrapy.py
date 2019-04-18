# -*- coding: utf-8 -*-
import scrapy


class FirstscrapySpider(scrapy.Spider):
    name = 'firstscrapy'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']

    def parse(self, response):
        pass

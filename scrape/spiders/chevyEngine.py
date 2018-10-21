# -*- coding: utf-8 -*-
import scrapy


class ChevyengineSpider(scrapy.Spider):
    name = 'chevyEngine'
    allowed_domains = ['summitracing.com']
    start_urls = ['http://summitracing.com/']

    def parse(self, response):
        pass

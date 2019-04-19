# -*- coding: utf-8 -*-
import scrapy


class TestingSpider(scrapy.Spider):
    name = 'testing'
    allowed_domains = ['https://www.firstweber.com/find-wisconsin-real-estate-agent']
    start_urls = ['http://https://www.firstweber.com/find-wisconsin-real-estate-agent/']

    def parse(self, response):
        for agent_url in response.css('.entry-title a::attr("href")').extract():
		yield response.follow(agent_url,callback=self.parse_agent)

    def parse_agent(self,response):
	content=response.xpath(".//div[@classs='entry-content']/descendant::text()").extract():
	yield {'article':''.join(content)}s

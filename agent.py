# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['https://www.firstweber.com/find-wisconsin-real-estate-agent']
    start_urls = ['http://https://www.firstweber.com/find-wisconsin-real-estate-agent/']

    def parse(self, response):
       for sel in response.xpath('//tbodytr'):
           item=agentsdetail()
           item['name']=scl.xpath('td@[class-"Darrell McDougal Realtor"]/a/text()').extract()
           item['url']=scl.xpath('td@[class-"https://www.firstweber.com/vp/AgentServlet?     SITE=FIRSTWEBER&ScreenID=AGENT_DETAIL_P&cd_Agent=89604"]/a/text()').extract()
           item['address']=scl.xpath('td@[class-"@type": , "N4128 Maple Dr.,Antigo,WI,54409"]/a/text()').extract()
           item['image_url']=scl.xpath('td@[class-"https://www.redata.com/100001/firstweber/agents/89604ax.jpg"]/a/text()').extract()
           item['name']=scl.xpath('td@[class-"Darrell McDougal Realtor"]/a/text()').extract()
           item['phone-number']=scl.xpath('td@[class-"715-610-5263"]/a/text()').extract()
           item['email']=scl.xpath('td@[class-email"]/a/span@[class="email"]/text()').extract()
           item['website']=scl.xpath('td@[class-"twitter:card" ]/a/text()').extract()
           item['bio']=scl.xpath('td@[class-"agent_bio"]/a/span@[class="bio"]/text()').extract()
           item['description']=scl.xpath('td@[class-""Darrell McDougal a 5.00 star agent in the Antigo Office.Homes for Sale in and around Antigo""]/a/text()').extract()
           yield item

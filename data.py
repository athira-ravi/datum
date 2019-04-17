# -*- coding: utf-8 -*-

response.xpath("//item/title").extract_first()

import scrapy


class DataSpider(scrapy.Spider):
    name = 'data'
    allowed_domains = ['https://www.firstweber.com/find-wisconsin-real-estate-agent']
    start_urls = ['http://https://www.firstweber.com/find-wisconsin-real-estate-agent/']

    def parse(self, response):
    	tiles=response.css('title::attr(title)'.extract()
	url=response.css('url::attr(url)'.extract()
	address=response.css('address::attr(address)'.extract()
        image=response.css('image::attr(image)'.extract() 
        telephone=response.css('telephone::attr(telephone)'.extract()
	email=response.css('email::attr(email)'.extract()
	website=response.css('website::attr(website)'.extract()
	social=response.css('social::attr(social)'.extract()
	agent_bio=response.css('agent_tile::attr(agent_bio)'.extract()
	description=response.css('description::attr(description)'.extract()

	for item in zip(titles,url,address,image,telephone,email,website,social,agent_bio,description):
		scraped_info={
			'title' : item[0]
			'url'   : item[1]
			'address' : item[0]
			'image' : item[1]
			'telephone' : item[2]
			'email' : item[3]
			'website' : item[4]
			'social' : item[5]
			'agent_bio' : item[6]
			'description' : item[7]
			}
			yield scraped_info



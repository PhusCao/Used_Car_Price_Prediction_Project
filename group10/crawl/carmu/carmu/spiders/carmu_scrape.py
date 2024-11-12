import scrapy
from carmu.items import CarmuItem
from datetime import datetime
import re
from functools import partial

from time import sleep
from json import dumps
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))
def tokafka(data):
    data = str(data)
    producer.send('testTopiccc', value=data)
class Fundrazr(scrapy.Spider):
	name = "carmudi"
		# First Start Url
	start_urls = ["https://www.carmudi.vn/mua-ban-o-to-cu/"]

	npages = 2
	# sokmm=0
	# This mimics getting the pages using the next button. 
	for i in range(2, npages + 17):#112->113
		start_urls.append("https://www.carmudi.vn/mua-ban-o-to-cu/index"+str(i)+".html")#https://www.carmudi.vn/mua-ban-o-to/index
	
	def parse(self, response):
		a=response.xpath("//div[contains(@class, 'list-info')]//div[contains(@class, 'list-info-detail-item')]/descendant::text()").extract()
		b=[3,19,35,51,67,83,99,115,131,147,163,179,195,211,227,243,259,275,291,307]
		c = [a[index] for index in b] 
		hrefs=response.xpath("//a[contains(@class, 'title is-5')]//@href")
		for href, sokm in zip(hrefs,c):
		#for href in response.xpath("//div[contains(@class, 'columns fr-container')]/a[contains(@class, 'title is-5')]//@href"):   response.xpath("//a[contains(@class, 'title is-5')]//@href").extract()
			# add the scheme, eg http://
			#url  = "https:" + href.extract()
			url  = href.extract()
			# self.sokmm=sokm
			yield scrapy.Request(url, callback=partial(self.parse_dir_contents, sokmm=sokm))#self.parse_dir_contents(response, sokm))	



					
	def parse_dir_contents(self, response, sokmm=None):
		item = CarmuItem()

		# Getting Campaign Title
		item['hang'] = response.xpath("//div[contains(@class, 'feature-item')]/descendant::text()").extract()[2].strip()

		# Getting Amount Raised
		item['giatien']= response.xpath("//div[contains(@class, 'price-tag')]/descendant::text()").extract()

		# Goal
		item['namsanxuat'] = response.xpath("//div[contains(@class, 'feature-item')]/descendant::text()").extract()[11].strip()

		# Currency Type (US Dollar Etc)
		item['nhienlieu'] = response.xpath("//div[contains(@class, 'feature-item')]/descendant::text()").extract()[21]

		# Campaign End (Month year etc)
		item['socho'] = response.xpath("//div[contains(@class, 'feature-item')]/descendant::text()").extract()[23]

		# Number of contributors
		item['xuatxu'] = response.xpath("//div[contains(@class, 'feature-item')]/descendant::text()").extract()[27]

		item['tinhtrang'] = response.xpath("//div[contains(@class, 'feature-item')]/descendant::text()").extract()[13]
		item['socua'] = response.xpath("//div[contains(@class, 'value')]/descendant::text()").extract()[1]
		item['hopso'] = response.xpath("//div[contains(@class, 'feature-item')]/descendant::text()").extract()[15]
		item['maunoithat'] = response.xpath("//div[contains(@class, 'feature-item')]/descendant::text()").extract()[25]
		item['kieudang'] = response.xpath("//div[contains(@class, 'feature-item')]/descendant::text()").extract()[19]
		item['tenxe'] = response.xpath("//h1[contains(@class, 'm-0 pages-title-name-detail')]/descendant::text()").extract()
		#item['diachi'] = response.xpath("//div[contains(@class, 'value')]/descendant::text()").extract()[57]
		item['diachi'] =response.xpath("//div[contains(@class,'tab_area location')]//div[contains(@class, 'value')]/descendant::text()").extract()[7]
		item['dongxe']=response.xpath("//div[contains(@class, 'feature-item')]/descendant::text()").extract()[6]  
		item['sokmdadi']=sokmm
		tokafka(item)
		yield item

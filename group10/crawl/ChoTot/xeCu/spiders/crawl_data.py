import scrapy
import json
from scrapy import Request

class OldCarSpider(scrapy.Spider):

    name = "crawl_ChoTot"
    start_urls = [''.join(['https://xe.chotot.com/mua-ban-oto?page=', str(i)]) for i in range(5)]

    def parse(self, response):

        x = (response.xpath('/html//div[@class = "ctAdlisting"]//ul//li//a[@href]').extract())
        for i in range(len(x)):
            y = (''.join(['https://xe.chotot.com/', x[i].split('>')[0].strip('<a href=').strip('"')]))
            if len(y.split()) == 1:
                yield Request(
                    url=y,
                    callback=self.abc
                )

    def abc(self, response):
        samples = []
        list_car_info = response.xpath('/html//div[@class = "media-body media-middle"]//span/text()').extract()
        car_info = dict()
        for i in range(int(len(list_car_info)/2)):
            car_info[list_car_info[2*i]] = list_car_info[2*i+1]
        car_info['dia diem'] = list_car_info[-1]
        price = (response.xpath('/html//span[@itemprop = "price"]/text()').extract())
        price = price[0]
        price = (int(''.join(e for e in price if e.isnumeric())))
        sample = {'car_info': car_info, 'price': price}
        # yield sample
        samples.append(sample)
        print(samples)
        # yield sample
        # print(sample)
        # self.data['data'].append(sample)
        # self.data['data'].append()

    
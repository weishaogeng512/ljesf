import scrapy
from ..items import LjesfItem

class ljesfSpider(scrapy.Spider):
    name = "ljesf"
    start_urls = ['https://xa.lianjia.com/ershoufang/pg2']

    def start_requests(self):
        return [scrapy.Request("https://xa.lianjia.com/ershoufang/pg{0}".format(x)) for x in range(2,36)]

    def parse(self, response):
        # print(response)
        ljesf = LjesfItem()
        title_list = response.xpath(".//div[@class='info clear']/div[@class='title']/a/text()").extract()  # 标题
        info_list1 = response.xpath(".//div[@class='houseInfo']") # 信息
        region_list = response.xpath(".//div[@class='info clear']/div[@class='flood']/div/a/text()").extract() # 区域
        totalprice_list = response.xpath(".//div[@class='info clear']/div[@class='priceInfo']/div[1]/span/text()").extract() # 总价
        price_list = response.xpath(".//div[@class='info clear']/div[@class='priceInfo']/div[2]/span/text()").extract() # 单价
        info_list =[item.xpath('string(.)').extract()[0] for item in info_list1]
        for i1, i2, i3, i4,i5 in zip(title_list, info_list, region_list, totalprice_list, price_list):
            ljesf['title'] = i1
            ljesf['info'] = i2
            ljesf['region'] = i3
            ljesf['totalprice'] = i4
            ljesf['price'] = i5
            yield ljesf
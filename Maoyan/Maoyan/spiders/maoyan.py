import scrapy
from Maoyan.items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
#    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/4?offset=10']

    def parse(self, response):
        items = MaoyanItem()
#       print("="*50)
#       a=1
        print(response.text)
        #print(response.xpath("//dl[@class='board-wrapper']//dd/a").extract())
        node_list = response.xpath("//dl[@class='board-wrapper']//dd")
#       print("222",node_list)
        for node in node_list:
#            a+=1
# print("1111",node)
            items['title'] = node.xpath(".//p[@class='name']/a/text()").extract()
            items['star'] = node.xpath(".//p[@class='star']/text()").extract()
            #print("-----{}-----{}".format(title[0],star[0]))
#           print("+"*50)
#       print("="*50,a)
            yield items

from scrapy import log
from scrapy.http import Request
import scrapy


class ZevenHeuvelItem(scrapy.Item):
    Plts = scrapy.Field()
    Naam = scrapy.Field()
    Woonplaats = scrapy.Field()
    Uitsl = scrapy.Field()
    Categ = scrapy.Field()
    Bruto = scrapy.Field()
    Netto = scrapy.Field()


class ZevenHeuvelSpider(scrapy.Spider):
    name = 'ZevenHeuvelSpider'
    allowed_domains = ['http://evenementen.uitslagen.nl']
    start_urls = ('http://evenementen.uitslagen.nl',)
    base_id = 1001
    max_id = 1234

    def start_requests(self):
            for i in range(self.base_id, self.max_id):
                yield Request('http://evenementen.uitslagen.nl/2016/zevenheuvelenloop/uitslag0'+str(i)+'.html',
                              callback=self.parse)

    def parse(self, response):
        global item
        log.msg('parse(%s)' % response.url, level=log.DEBUG)
        rows = response.xpath('//table[@class="i"]/tr')
        for row in rows:
            item = ZevenHeuvelItem()
            item['Plts'] = row.xpath('td[1]/text()').extract()
            item['Naam'] = row.xpath('td[2]/a/text()').extract()
            item['Woonplaats'] = row.xpath('td[3]/text()').extract()
            item['Uitsl'] = row.xpath('td[5]/text()').extract()
            item['Categ'] = row.xpath('td[6]/text()').extract()
            item['Bruto'] = row.xpath('td[7]/text()').extract()
            item['Netto'] = row.xpath('td[8]/text()').extract()
            yield item

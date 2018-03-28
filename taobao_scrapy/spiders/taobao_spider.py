import scrapy


class TaobaoSpider(scrapy.Spider):
    name = "taobao"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'https://shoucang.taobao.com/item_collect_n.htm?tab=0&t=1521781882638'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

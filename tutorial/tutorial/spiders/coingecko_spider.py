import json
import scrapy
from ..items import TutorialItem


class CoingeckoSpiderSpider(scrapy.Spider):
    name = 'coingecko_spider'
    allowed_domains = ['coingecko.com']
    start_urls = ['http://coingecko.com/']

    def parse(self, response):
        items = TutorialItem()

        coin_name = response.css('tr:nth-child(1) .font-bold').extract()
        coin_price = response.css('tr:nth-child(1) .tw-flex-1 .no-wrap').extract()

        nm_out = coin_name[0].replace('<span class="lg:tw-flex font-bold tw-items-center tw-justify-between">\n', '')
        cn_out = coin_price[0].replace('<span class=\"no-wrap\" data-price-btc=\"1.0\" data-coin-id=\"1\" data-coin-symbol=\"btc\" data-target=\"price.price\">', '')

        items["coin_name"] = nm_out.replace('\n</span>', '')
        items["coin_price"] = cn_out.replace('</span>', '')

        yield items

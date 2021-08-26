import scrapy

from clothes_spider.product_item import ProductItem
from clothes_spider.urls import URLS


class SheegoSpider(scrapy.Spider):
    name = 'sheego_scrapping'
    allowed_domains = ['sheego.de']
    start_urls = URLS
            
    def parse(self, response):
        for product in response.css('section.cj-product.js-product-box.js-product-box--list.js-unveil-plbox.at-product-box'):
            product_item = {
                    'title': product.css('div.product__title.at-pl-item-title::text').extract_first(),
                    'price': product.css('span.product__price--normal.l-bold.l-mr-5::text').extract_first(),
                    'image_url': product.css('img.cj-product__image.js-unveil-plbox-child.at-pl-item-image::attr(data-src)').extract_first()
            }
            yield ProductItem(title = product_item['title'], price = product_item['price'], 
                image_urls = ['https:{image_url}'.format(image_url = product_item['image_url'])])

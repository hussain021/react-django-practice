import scrapy

from clothes_spider.items import ImageItem


class ImageSpider(scrapy.Spider):
    name = 'clothes_scrapping'
    allowed_domains = ['sheego.de']
    start_urls = ['https://www.sheego.de/damenmode/jeans/']
    name = "clothes_spider"

    def parse(self, response):
        for cloth in response.css('section.cj-product.js-product-box.js-product-box--list.js-unveil-plbox.at-product-box'):
            item = {
                    'title': cloth.css('div.product__title.at-pl-item-title::text').extract_first(),
                    'price': cloth.css('span.product__price--normal.l-bold.l-mr-5::text').extract_first(),
                    'image_url': cloth.css('img.cj-product__image.js-unveil-plbox-child.at-pl-item-image::attr(data-src)').extract_first()
            }
            yield ImageItem(title = item['title'], price = item['price'], image_urls = ['https:'+item['image_url']])
            
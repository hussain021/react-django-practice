import scrapy

from clothes_spider.product_item import ProductItem
from clothes_spider.urls import URLS


class SheegoSpider(scrapy.Spider):
    name = 'sheego_scrapping'
    allowed_domains = ['sheego.de']
    start_urls = URLS
            
    def parse(self, response):
        """This function collects the urls of all the products mentioned in the starting urls"""
        for product in response.css(
                'section.cj-product.js-product-box.js-product-box--list.js-unveil-plbox.at-product-box'
                ):
            single_product_url = {'url': product.css('a.js-product__link::attr(href)').extract_first()}
            yield scrapy.Request(url='https://sheego.de/{product_url}'.format(
                product_url=single_product_url['url']),
                callback=self.parse_product
                )

    def parse_product(self, response):
        """This function scraps the detail of each product using the url that has been passed to it

            this function yields the data in form of ProductItem and stores the images in the images
            folder.
        """
        product_details = {
            'title': response.css('span.p-details__name.l-text-1.at-name::text').extract_first(),
            'price': response.css('span.l-subline-2.l-bold.product__price__current.at-lastprice::text').extract_first(),
            'all_sizes': response.css('div.sizespots__item.js-click-variant.at-dv-size-button::text').extract(),
            'image_urls': response.css('span.l-pointer::attr(data-image)').extract(),
            'all_colors': response.css(
                'div.cj-slider__item.js-click-variant.at-dv-color.colorspots__item > img.js-slider__unveil::attr(alt)'
                ).extract(),
            'description': response.css('div.details__box__desc.at-dv-artDes.l-pr-10 > p::text').extract_first(),
        }
        yield ProductItem(
            title = product_details['title'],
            price = product_details['price'], 
            image_urls = [
                'https:{image_url}'.format(
                image_url=product_details['image_urls'][index])
                for index, url in enumerate(product_details['image_urls'])
                ],
            all_sizes = product_details['all_sizes'],
            all_colors = product_details['all_colors'],
            description = product_details['description'],
            )

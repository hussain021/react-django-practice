import scrapy

from clothes_spider.product_item import ProductItem
from clothes_spider.urls import URLS


class SheegoSpider(scrapy.Spider):
    name = "sheego_scrapping"
    allowed_domains = ["sheego.de"]
    start_urls = URLS

    def parse(self, response):
        """This function collects the urls of all the products mentioned in the starting urls"""
        for product in response.css(
            "section.cj-product.js-product-box.js-product-box--list.js-unveil-plbox.at-product-box"
        ):
            single_product_url = self._get_single_product_url(product)
            yield scrapy.Request(
                url="https://sheego.de/{product_url}".format(
                    product_url=single_product_url
                ),
                callback=self.parse_product,
            )

    def parse_product(self, response):
        """This function scraps the detail of each product using the url that has been passed to it

        this function yields the data in form of ProductItem and stores the images in the images
        folder.
        """
        yield ProductItem(
            title=self._clean([self._get_title(response)])[0],
            price=eval(
                [size.replace(",", ".") for size in [self._get_price(response)[:-2]]][0]
            ),
            currency=self._clean([self._get_price(response)[-2:]])[0],
            image_urls=self._format_image_urls(self._get_image_urls(response)),
            all_sizes=[
                eval(size) for size in self._clean(self._get_all_sizes(response))
            ],
            all_colors=self._clean(self._get_all_colors(response)),
            description=self._clean([self._get_description(response)])[0],
        )

    def _get_single_product_url(self, product):
        return product.css("a.js-product__link::attr(href)").extract_first()

    def _get_title(self, response):
        return response.css(
            "span.p-details__name.l-text-1.at-name::text"
        ).extract_first()

    def _get_price(self, response):
        return response.css(
            "span.l-subline-2.l-bold.product__price__current.at-lastprice::text"
        ).extract_first()

    def _get_all_sizes(self, response):
        return response.css(
            "div.sizespots__item.js-click-variant.at-dv-size-button::text"
        ).extract()

    def _get_image_urls(self, response):
        return response.css("span.l-pointer::attr(data-image)").extract()

    def _get_all_colors(self, response):
        return response.css(
            "div.cj-slider__item.js-click-variant.at-dv-color.colorspots__item > img.js-slider__unveil::attr(alt)"
        ).extract()

    def _get_description(self, response):
        return response.css(
            "div.details__box__desc.at-dv-artDes.l-pr-10 > p::text"
        ).extract_first()

    def _clean(self, string_list: list):
        return list(map(str.strip, string_list))

    def _format_image_urls(self, image_urls):
        return [
            "https:{image_url}".format(image_url=image_urls[index])
            for index, url in enumerate(image_urls)
        ]

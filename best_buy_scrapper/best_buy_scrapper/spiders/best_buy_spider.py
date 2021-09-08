import json
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from datetime import datetime

from best_buy_scrapper.items import ProductItem


class BestBuySpider(CrawlSpider):
    name = "best_buy_spider"
    allowed_domains = [
        "bestbuy.com",
        "pisces.bbystatic.com",
    ]  # Second link is where images are accessed.
    start_urls = ["https://www.bestbuy.com/"]
    rules = [
        Rule(LinkExtractor(allow="site/"), callback="parse_product", follow=True)
    ]

    def parse_product(self, response):
        is_product = response.css(
            "a.c-button-link.c-button.btn-brand-link::text"
        ).extract_first()
        if is_product:
            skus = response.xpath(
                '//script[contains(text(),"priceCurrency")]/text()'
            ).extract_first()
            skus = json.loads(skus)
            yield ProductItem(
                language=self.get_language(response),
                category=self.get_categories(response),
                brand=self.get_brand(response),
                url=response.url,
                scraped_date=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                title=self.get_title(response),
                description=self.get_description(response),
                specification=self.get_specifications(response),
                image_urls=self.get_image_urls(response),
                skus=self.get_skus_details(skus),
            )

    def get_skus_details(self, skus):
        return {
            "price": float(skus["offers"]["price"])
            if skus["offers"].get("price")
            else None,
            "currency": skus["offers"]["priceCurrency"],
            "color": skus["color"] if skus.get("color") else None,
            "availability": True
            if (
                skus["offers"]["availability"]
                if skus["offers"].get("availability")
                else ""
            )
            in "InStock"
            else False,
            "sku_id": skus["sku"],
        }

    def get_language(self, response):
        return response.css("html::attr(lang)").extract_first()

    def get_categories(self, response):
        return response.css("li.c-breadcrumbs-list-item > a::text").extract()

    def get_brand(self, response):
        return response.css(
            "a.c-button-link.c-button.btn-brand-link::text"
        ).extract_first()

    def get_title(self, response):
        return response.css("h1.heading-5.v-fw-regular::text").extract_first()

    def get_description(self, response):
        desc_using_way_prod = response.css("div.product-description::text").extract_first()
        desc_using_html_frag = response.css(
            "div.html-fragment > div > div::text"
        ).extract_first()
        return desc_using_way_prod if desc_using_way_prod is not None else desc_using_html_frag

    def get_specifications(self, response):
        titles = response.css(
            "div.row-title::text, div.row-title > span.display-name.v-fw-medium.body-copy::text"
        ).extract()
        titles = list(filter(lambda title: title != " ", titles))
        values = response.css("div.row-value.col-xs-6.v-fw-regular::text").extract()
        return {titles[index]: values[index] for index in range(len(titles))}

    def get_image_urls(self, response):
        return [response.css("img.primary-image::attr(src)").extract_first()]

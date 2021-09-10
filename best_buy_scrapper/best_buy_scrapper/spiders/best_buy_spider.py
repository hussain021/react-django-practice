from http.cookiejar import Cookie
import json
from datetime import datetime
from itemloaders import ItemLoader
import scrapy
from scrapy.http.cookies import CookieJar

from best_buy_scrapper.menu_link import MenuLink
from best_buy_scrapper.items import ProductItem


class BestBuySpider(scrapy.Spider):

    name = "best_buy_spider"
    allowed_domains = [
        "www.bestbuy.com",
        "pisces.bbystatic.com",
    ]  # Second link is where images are accessed.
    menu_link = MenuLink()
    start_urls= menu_link.list_of_links

    def parse(self, response):
        """Initiator for the spider, Where cookies are added to the request.

        Keyword arguments:
        response -- contains the response of the starting urls
        """
        cookieJar = response.meta.setdefault("cookie_jar", CookieJar())
        cookieJar.set_cookie(
            cookie=Cookie(
                name="intl_splash",
                value="false",
                path="/",
                domain="www.bestbuy.com",
                expires=None,
                version=0,
                port=None,
                port_specified=False,
                domain_specified=True,
                domain_initial_dot=False,
                path_specified=True,
                secure=False,
                discard=True,
                comment=None,
                comment_url=None,
                rest={"HttpOnly": None},
            )
        )
        cookieJar.extract_cookies(response, response.request)
        request = self.send_request(response.url, self.parse_list_of_products, cookieJar)
        yield request

    def parse_list_of_products(self, response):
        """Get the list of products from the page.

        Keyword arguments:
        response -- contains the response of the the page which contains multiple products
        """
        product_url_list = response.css("h4.sku-header > a::attr(href)").extract()
        if len(product_url_list) == 0:#There are two types of Product listings, If one is empty, Choose the other
             product_url_list=response.css("a.wf-offer-link.v-line-clamp ::attr(href)").extract()
            
        product_url_list = ['https://www.bestbuy.com/{}'.format(link) for link in product_url_list]
        cookie_jar = response.meta.setdefault("cookie_jar", CookieJar())
        cookie_jar.extract_cookies(response, response.request)
        for product_url in product_url_list:
            request = self.send_request(product_url, self.parse_product, cookie_jar)#function to send request with cookies
            yield request

    def parse_product(self, response):
        """Get the details of the product

        Keyword arguments:
        response -- contains the response of the the page which product details
        """
        product = ItemLoader(item=ProductItem(), response=response)
        is_product = response.css(
            "a.c-button-link.c-button.btn-brand-link::text"
        ).extract_first()
        if is_product:
            skus = response.xpath(
                '//script[contains(text(),"priceCurrency")]/text()'
            ).extract_first()
            skus = json.loads(skus)
            product.add_value("language", self.get_language(response))
            product.add_value("category", self.get_categories(response))
            product.add_value("brand", self.get_brand(response))
            product.add_value("url", response.url)
            product.add_value(
                "scraped_date", datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            )
            product.add_value("title", self.get_title(response))
            product.add_value("description", self.get_description(response))
            product.add_value("specification", self.get_specifications(response))
            product.add_value("image_urls", self.get_image_urls(response))
            product.add_value("skus", self.get_skus_details(skus))

            return product.load_item()

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
        desc_using_way_prod = response.css(
            "div.product-description::text"
        ).extract_first()
        desc_using_html_frag = response.css(
            "div.html-fragment > div > div::text"
        ).extract_first()
        return (
            desc_using_way_prod
            if desc_using_way_prod is not None
            else desc_using_html_frag
        )

    def get_specifications(self, response):
        titles = response.css(
            "div.row-title::text, div.row-title > span.display-name.v-fw-medium.body-copy::text"
        ).extract()
        titles = list(filter(lambda title: title != " ", titles))
        values = response.css("div.row-value.col-xs-6.v-fw-regular::text").extract()
        return {titles[index]: values[index] for index in range(len(titles))}

    def get_image_urls(self, response):
        return [response.css("img.primary-image::attr(src)").extract_first()]

    def send_request(self, url, callback, cookie_jar):
        request = scrapy.Request(
            url,
            callback=callback,
            meta={"dont_merge_cookies": True, "cookie_jar": cookie_jar},
                )
        cookie_jar.add_cookie_header(request)
        return request

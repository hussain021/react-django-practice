from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from games_scrapper.items import GameItem


class StreamSpider(CrawlSpider):
    name = "spider"
    allowed_domains = ["store.steampowered.com"]
    start_urls = ["https://store.steampowered.com/"]
    base_url = "https://store.steampowered.com/"
    rules = [
        Rule(
            LinkExtractor(
                allow="https://store.steampowered.com/app/",
                deny=[
                    "/?l=",
                ],
            ),
            callback="parse",
            follow=True,
        )
    ]
    """
    This is the parse function

    Args:
        param1: self
        param2: response

    Returns:
        yields the items scraped

    """

    def parse(self, response):
        game_item = GameItem(
            name=self.get_name(response),
            description=self.get_description(response),
            all_reviews=self.get_all_reviews(response),
            all_reviews_count=self.get_all_reviews_count(response),
            release_date=self.get_release_date(response),
            developer=self.get_developer(response),
            publisher=self.get_publisher(response),
        )
        image_url_list = self.get_image_urls(response)
        items = {
            "game_item": game_item,
            "image_urls": image_url_list,
        }
        yield items

    """
    This function gets the image urls from the site and then removes the size from the url

    Args:
        param1: self
        param2: response

    Returns:
       Returns the urls of the image.

    """

    def get_image_urls(self, response):
        image_urls = response.css(
            "div.highlight_strip_item.highlight_strip_screenshot > img::attr(src)"
        ).extract()
        # sample url
        # https://cdn.akamai.steamstatic.com/steam/apps/1031120/ss_5be7930883200d7870ef279cbefe05e8f6ff48f2.1920x1080.jpg?t=1634223750
        # following code removes the size i.e .1920x1080 in the above example for all images.
        for index, url in enumerate(image_urls):
            end_index = url.rfind(".")
            start_index = url[0:end_index].rfind(".")
            part_two = url[end_index:]
            part_one = url[0:start_index]
            image_urls[index] = part_one + part_two
        return image_urls

    """
    This function gets the name of the game

    Args:
        param1: self
        param2: response

    Returns:
       Returns the name of the game.

    """

    def get_name(self, response):
        return self.clean(response.css("div.apphub_AppName::text").extract_first())

    """
    This function gets the description of the game

    Args:
        param1: self
        param2: response

    Returns:
       Returns the description of the game.

    """

    def get_description(self, response):
        desc = response.css("div.game_description_snippet::text").extract_first()
        if desc is None:
            desc = response.css("div.glance_details > p::text").extract_first()
        return self.clean(desc)

    """
    This function gets all reviews of the game

    Args:
        param1: self
        param2: response

    Returns:
       Returns all reviews of the game.

    """

    def get_all_reviews(self, response):
        all_reviews = response.xpath(
            '//*[@id="userReviews"]/div/div[2]/span[1]/text()'
        ).extract_first()
        if all_reviews is None:
            all_reviews = response.xpath(
                '//*[@id="userReviews"]/div/div[2]/text()'
            ).extract_first()
        return self.clean(all_reviews)

    """
    This function gets review total count of the game

    Args:
        param1: self
        param2: response

    Returns:
       Returns the total review count of the game.

    """

    def get_all_reviews_count(self, response):
        all_reviews_count = response.css("span.responsive_hidden::text").extract_first()
        if all_reviews_count is None or all_reviews_count is ":":
            return "0"
        return self.clean(all_reviews_count)

    """
    This function gets the release date of the game

    Args:
        param1: self
        param2: response

    Returns:
       Returns the release date of the game.

    """

    def get_release_date(self, response):
        return self.clean(response.css("div.date::text").extract_first())

    """
    This function gets the developer name of the game

    Args:
        param1: self
        param2: response

    Returns:
       Returns the developer name of the game.

    """

    def get_developer(self, response):
        return self.clean(response.css("#developers_list > a::text").extract_first())

    """
    This function gets the publisher name of the game

    Args:
        param1: self
        param2: response

    Returns:
       Returns the publisher name of the game.

    """

    def get_publisher(self, response):
        publisher = response.css(
            "#game_highlights > div.rightcol > div > div.glance_ctn_responsive_left > div:nth-child(4) > div.summary.column > a::text"
        ).extract_first()
        if publisher is None:
            return ""
        return self.clean(publisher)

    """
    This function cleans the data gathered from the website(removes \t, \n etc)

    Args:
        param1: self
        param2: str

    Returns:
       Returns the cleaned string.

    """

    def clean(self, str):
        return str.strip()

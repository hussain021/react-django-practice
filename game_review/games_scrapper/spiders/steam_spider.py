from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import scrapy
from games_scrapper.items import GameItem


class SteamSpider(CrawlSpider):
    name = "spider"
    allowed_domains = ["store.steampowered.com"]
    start_urls = ["https://store.steampowered.com/"]
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

    def parse(self, response):
        """
        This is the parse function

        Args:
            param1: self
            param2: response

        Returns:
            yields the game and image items.

        """
        game_id = self.get_game_id(response.url)
        poster_image = (self.get_poster_image(response),)
        game_item = GameItem(
            game_id=game_id,
            name=self.get_name(response),
            description=self.get_description(response),
            all_reviews_ratings=self.get_all_reviews(response),
            all_reviews_count=self.get_all_reviews_count(response),
            release_date=self.get_release_date(response),
            developer=self.get_developer(response),
            publisher=self.get_publisher(response),
            poster_image=str(poster_image[0]),
        )
        image_url_list = self.get_image_urls(response) + [str(poster_image[0])]
        url = self.get_review_url(game_id)
        yield {
            "type": "game",
            "game_item": game_item,
            "image_urls":[str(poster_image[0])]
            #"image_urls": image_url_list,
        }
        yield scrapy.Request(
            url=url, callback=self.parse_review, dont_filter=True, meta={"id": game_id}
        )

    def parse_review(self, response):
        """
        This is a parse function

        Args:
            param1: self
            param2: response

        Returns:
            yields the review item

        """
        reviews = self.get_review_text_list(response)
        reviews_is_recommended = self.get_review_is_recommended_list(response)
        reviews_posted_date = self.get_review_posted_date_list(response)
        review_posted_by = self.get_review_posted_by_list(response)
        for index, review in enumerate(reviews):
            yield {
                "id": response.meta["id"],
                "type": "review",
                "is_recommended": self.get_review_is_recommended(
                    reviews_is_recommended[index]
                ),
                "posted_date": self.clean(reviews_posted_date[index]),
                "posted_by": self.clean(review_posted_by[index]),
                "text": self.clean(review),
            }

    def get_image_urls(self, response):
        """
        This function gets the image urls from the site and then removes the size from the url

        Args:
            param1: self
            param2: response

        Returns:
        Returns the urls of the image.

        """
        image_urls = response.css(
            "div.highlight_strip_item.highlight_strip_screenshot > img::attr(src)"
        ).extract()
        for index, url in enumerate(image_urls):
            image_urls[index] = self.get_image_url_without_size(url)

        return image_urls

    def get_image_url_without_size(self, url):
        """
        This function removes the size i.e .1920x1080 in the below example for the url passed:
        https://cdn.akamai.steamstatic.com/steam/apps/1031120/ss_5be7930883200d7870ef279cbefe05e8f6ff48f2.1920x1080.jpg?t=1634223750


        Args:
            param1: self
            param2: url

        Returns:
        Returns url of image without size.

        """
        after_size_index = url.rfind(".")
        before_size_index = url[0:after_size_index].rfind(".")
        after_size_url = url[after_size_index:]
        before_size_url = url[0:before_size_index]
        return before_size_url + after_size_url

    def get_name(self, response):
        """
        This function gets the name of the game

        Args:
            param1: self
            param2: response

        Returns:
        Returns the name of the game.

        """
        return self.clean(response.css("div.apphub_AppName::text").extract_first())

    def get_description(self, response):
        """
        This function gets the description of the game

        Args:
            param1: self
            param2: response

        Returns:
        Returns the description of the game.

        """
        desc = response.css("div.game_description_snippet::text").extract_first()
        if desc is None:
            desc = response.css("div.glance_details > p::text").extract_first()

        return self.clean(desc)

    def get_all_reviews(self, response):
        """
        This function gets all reviews of the game

        Args:
            param1: self
            param2: response

        Returns:
        Returns all reviews of the game.

        """
        all_reviews = response.xpath(
            '//*[@id="userReviews"]/div/div[2]/span[1]/text()'
        ).extract_first()
        if all_reviews is None:
            all_reviews = response.xpath(
                '//*[@id="userReviews"]/div/div[2]/text()'
            ).extract_first()

        return self.clean(all_reviews)

    def get_all_reviews_count(self, response):
        """
        This function gets review total count of the game

        Args:
            param1: self
            param2: response

        Returns:
        Returns the total review count of the game.

        """
        all_reviews_count = response.css("span.responsive_hidden::text").extract_first()
        if all_reviews_count is None or all_reviews_count == ":":
            return "0"

        return self.clean(all_reviews_count)

    def get_release_date(self, response):
        """
        This function gets the release date of the game

        Args:
            param1: self
            param2: response

        Returns:
        Returns the release date of the game.

        """
        return self.clean(response.css("div.date::text").extract_first())

    def get_poster_image(self, response):
        """
        This function gets the poster image of the game

        Args:
            param1: self
            param2: response

        Returns:
        Returns the main image of the game.

        """
        return response.css(
            "div.game_header_image_ctn > img::attr(src)"
        ).extract_first()

    def get_developer(self, response):
        """
        This function gets the developer name of the game

        Args:
            param1: self
            param2: response

        Returns:
        Returns the developer name of the game.

        """
        return self.clean(response.css("#developers_list > a::text").extract_first())

    def get_publisher(self, response):
        """
        This function gets the publisher name of the game

        Args:
            param1: self
            param2: response

        Returns:
        Returns the publisher name of the game.

        """
        publisher = response.css(
            "#game_highlights > div.rightcol > div > div.glance_ctn_responsive_left > div:nth-child(4) > div.summary.column > a::text"
        ).extract_first()
        return self.clean(publisher)

    def clean(self, str):
        """
        This function cleans the data gathered from the website(removes \t, \n etc)

        Args:
            param1: self
            param2: str

        Returns:
        Returns the cleaned string.

        """
        if str is not None:
            return str.strip()

        return ""

    def get_game_id(self, url):
        """
        This function gets the game_id from the url for later use

        Args:
            param1: self
            param2: str

        Returns:
        Returns the game_id in form of string

        """
        start_index = url.find("app/") + 4  # adding 4 for 4 letters i.e 'app/'
        end_index = start_index + url[start_index:].find("/")
        return url[start_index:end_index]

    def get_review_url(self, game_id):
        """
        This function returns the url for reviews of the game.

        Args:
            param1: self
            param2: game_id

        Returns:
        Returns the url for review of the game with game_id

        """
        # Wanted to use constants for the url, but couldn't due to .format
        return "https://steamcommunity.com/app/{}/reviews/".format(game_id)

    def get_review_is_recommended_list(self, response):
        """
        This function the list of recommended or not recommended from the review page

        Args:
            param1: self
            param2: response

        Returns:
        Returns a list of string with 'Recommended' or 'Not Recommended'

        """
        return response.css("div.title::text").extract()

    def get_review_is_recommended(self, is_recommended):
        """
        This function returns true if str is "Recommended" else false

        Args:
            param1: self
            param2: is_recommended

        Returns:
        Returns the url for review of the game with game_id

        """
        if self.clean(is_recommended) == "Recommended":
            return True

        return False

    def get_review_posted_date_list(self, response):
        """
        This function returns a list of posted date for the reviews

        Args:
            param1: self
            param2: response

        Returns:
        Returns a list with posted dates

        """
        return response.css("div.date_posted::text").extract()

    def get_review_text_list(self, response):
        """
        This function returns a list of text for the reviews

        Args:
            param1: self
            param2: response

        Returns:
        Returns a list with text

        """
        return response.css("div.apphub_CardTextContent::text").extract()

    def get_review_posted_by_list(self, response):
        """
        This function returns a list of author names for the reviews

        Args:
            param1: self
            param2: response

        Returns:
        Returns a list with author names

        """
        return response.css("div.apphub_CardContentAuthorName > a::text").extract()

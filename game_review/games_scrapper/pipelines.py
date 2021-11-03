# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import hashlib
from scrapy.exceptions import DropItem
from django.shortcuts import get_object_or_404

from backend.models import Game, Review, Image
from games_scrapper.items import ImageItem, ReviewItem


class GamesScrapperPipeline:
    def process_item(self, item, spider):
        if item["type"] == "review":
            id = item["id"]
            game_object = get_object_or_404(Game, game_id=id)
            review_item = ReviewItem(
                is_recommended=item["is_recommended"],
                posted_date=item["posted_date"],
                text=item["text"],
                posted_by=item["posted_by"],
            )
            review_item.save()
            review_item = get_object_or_404(Review, text=item["text"])
            game_object.reviews.add(review_item)
            game_object.save()
        else:
            game_item = item["game_item"]
            if (
                game_item["description"] != "This content requires the base game"
                and game_item["description"] != "This is additional content for"
            ):
                game_item["all_reviews_ratings"] = self.get_rating(
                    game_item["all_reviews_ratings"]
                )
                game_item["all_reviews_count"] = self.get_reviews_count(
                    game_item["all_reviews_count"]
                )
                poster_image_path = (
                    hashlib.sha1(game_item["poster_image"].encode("utf-8")).hexdigest()
                ) + ".jpg"
                poster_image = ImageItem(image_path=poster_image_path)
                poster_image.save()
                poster_image = get_object_or_404(Image, image_path=poster_image_path)
                game_item["poster_image"] = poster_image
                game_item.save()
                game_object = Game.objects.get(name=game_item["name"])
                image_items = item["image_urls"]
                for image in image_items:
                    image_path = (
                        hashlib.sha1(image.encode("utf-8")).hexdigest()
                    ) + ".jpg"
                    image_item = ImageItem(
                        image_path=image_path,
                    )
                    image_item.save()
                    image_item = get_object_or_404(Image, image_path=image_path)
                    game_object.images.add(image_item)
                return item
            else:
                raise DropItem(f"{item} is not a Game")

    def get_rating(self, review):
        if review == "Overwhelmingly Positive":
            return "7"
        elif review == "Very Positive":
            return "6"
        elif review == "Mostly Positive":
            return "5"
        elif review == "Mixed":
            return "4"
        elif review == "Mostly Negative":
            return "3"
        elif review == "Very Negative":
            return "2"
        elif review == "Overwhelmingly Negative":
            return "1"
        else:
            return "0"

    def get_reviews_count(self, review_count):
        replacements = {"(": "", ")": ""}
        for replace, replace_with in replacements.items():
            review_count = review_count.replace(replace, replace_with)
        return review_count

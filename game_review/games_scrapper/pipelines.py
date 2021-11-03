# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import hashlib

from backend.models import Game
from games_scrapper.items import ImageItem, ReviewItem


class GamesScrapperPipeline:
    def process_item(self, item, spider):
        if item["type"] is "review":
            id = item["id"]
            game_object = Game.objects.get(id=id)
            review_item = ReviewItem(
                is_recommended=item["is_recommended"],
                posted_date=item["posted_date"],
                text=item["text"],
                game_id=game_object,
            )
            review_item.save()
        else:
            game_item = item["game_item"]
            game_item.save()
            game_object = Game.objects.get(name=game_item["name"])
            image_items = item["image_urls"]
            for image in image_items:
                image_item = ImageItem(
                    image_path=(hashlib.sha1(image.encode("utf-8")).hexdigest())
                    + ".jpg",
                    game_id=game_object,
                )
                image_item.save()
            return item

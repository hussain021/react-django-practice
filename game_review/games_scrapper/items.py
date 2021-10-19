# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import os
import django
from scrapy_djangoitem import DjangoItem


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "game_review.settings")
django.setup()

from backend.models import Game, Image, Review


class GameItem(DjangoItem):
    django_model = Game


class ImageItem(DjangoItem):
    django_model = Image


class ReviewItem(DjangoItem):
    django_model = Review

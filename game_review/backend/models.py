from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(AbstractUser):
    username = models.CharField(
        max_length=30,
        unique=True,
    )


class Image(BaseModel):
    image_path = models.CharField(primary_key=True, max_length=255)


class Game(BaseModel):
    game_id = models.IntegerField(verbose_name="Game ID", unique=True)
    name = models.TextField(verbose_name="game_title")
    description = models.TextField(verbose_name="game_description")
    images = models.ManyToManyField("Image", related_name="images")
    reviews = models.ManyToManyField("Review", related_name="reviews")
    all_reviews_ratings = models.CharField(max_length=40)
    all_reviews_count = models.CharField(max_length=30)
    release_date = models.CharField(max_length=40)
    developer = models.CharField(max_length=40)
    publisher = models.CharField(max_length=40)
    poster_image = models.ForeignKey(Image, on_delete=models.CASCADE)


class Review(BaseModel):
    is_recommended = models.BooleanField(default=True)
    posted_date = models.CharField(max_length=40)
    posted_by = models.CharField(max_length=40)
    text = models.TextField(verbose_name="review_text", unique=True)

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE


class User(AbstractUser):
    username = models.CharField(
        ("username"),
        max_length=30,
        unique=True,
    )


class Game(models.Model):
    id = models.AutoField(verbose_name="id", primary_key=True)
    name = models.TextField(verbose_name="game", unique=True)
    description = models.TextField(verbose_name="game_description")
    all_reviews = models.CharField(verbose_name="all_reviews", max_length=20)
    all_reviews_count = models.CharField(verbose_name="all_review_count", max_length=10)
    release_date = models.CharField(verbose_name="release_date", max_length=40)
    developer = models.CharField(verbose_name="developer", max_length=40)
    publisher = models.CharField(verbose_name="publisher", max_length=40)


class Review(models.Model):
    id = models.AutoField(verbose_name="review_id", primary_key=True)
    is_recommended = models.BooleanField(verbose_name="is_recommended", default=True)
    posted_date = models.DateField(verbose_name="posted_date")
    text = models.TextField(verbose_name="text")
    game_id = models.ForeignKey(
        verbose_name="game_id", to=Game, on_delete=models.CASCADE
    )


class Image(models.Model):
    id = models.AutoField(verbose_name="image_id", primary_key=True)
    image_path = models.CharField(verbose_name="image_path", max_length=255)
    game_id = models.ForeignKey(
        verbose_name="game_id", to=Game, on_delete=models.CASCADE
    )

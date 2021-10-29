from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE


class User(AbstractUser):
    username = models.CharField(
        max_length=30,
        unique=True,
    )

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Game(BaseModel, models.Model):
    id = models.IntegerField(verbose_name="game_id", primary_key=True)
    name = models.TextField(verbose_name="game_title", unique=True)
    description = models.TextField(verbose_name="game_description")
    images = models.ManyToManyField("Image", related_name="images")
    reviews = models.ManyToManyField("Review", related_name='reviews')
    all_reviews_ratings = models.CharField(max_length=40)
    all_reviews_count = models.CharField(max_length=30)
    release_date = models.CharField( max_length=40)
    developer = models.CharField( max_length=40)
    publisher = models.CharField( max_length=40)
    poster_image = models.CharField(verbose_name="poster_image_path", max_length=255)



class Review(BaseModel, models.Model):
    id = models.AutoField(verbose_name="review_id", primary_key=True)
    is_recommended = models.BooleanField( default=True)
    posted_date = models.CharField( max_length=40)
    text = models.TextField(verbose_name="review_text")
    game_id = models.ForeignKey(
        verbose_name="game_id", to=Game, on_delete=models.CASCADE
    )


class Image(BaseModel, models.Model):
    id = models.AutoField(verbose_name="image_id", primary_key=True)
    image_path = models.CharField(max_length=255)
    game_id = models.ForeignKey(
        verbose_name="game_id", to=Game, on_delete=models.CASCADE
    )

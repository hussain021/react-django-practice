from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(("username"), max_length=30, unique=True,)


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    note_title = models.CharField(max_length=30, null=True, default="")
    note_text = models.CharField(max_length=100)
    created_date = models.DateTimeField("date created")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    visibility = models.BooleanField(default=True)

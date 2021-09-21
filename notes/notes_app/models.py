from django.contrib.auth.models import AbstractUser
from django.db import models

from notes_app.constants import VISIBILITY


class User(AbstractUser):
    username = models.CharField(("username"), max_length=30, unique=True,)


class Note(models.Model):
    id = models.AutoField(verbose_name="id", primary_key=True)
    note_title = models.CharField(
        verbose_name="note title", max_length=30, null=True, default=""
    )
    note_text = models.CharField(verbose_name="note text", max_length=100)
    created_date = models.DateTimeField(verbose_name="date created", auto_now=True)
    created_by = models.ForeignKey(
        verbose_name="created by", to=User, on_delete=models.CASCADE
    )
    visibility = models.CharField(
        max_length=10, verbose_name="visibility", default=True, choices=VISIBILITY
    )

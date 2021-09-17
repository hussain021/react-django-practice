from django.contrib import admin

from .models import Note, User

admin.site.register(User)
admin.site.register(Note)

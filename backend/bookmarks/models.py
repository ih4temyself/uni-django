from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model


class Category(Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name


class Bookmark(Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name="bookmarks"
    )
    url = models.URLField()
    title = models.CharField(max_length=180)
    category = models.ForeignKey(
        Category,
        related_name="bookmarks",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title

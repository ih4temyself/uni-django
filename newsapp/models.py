from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author_news", args=[str(self.id)])


class News(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="news")
    publication_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.title} {self.author} {self.publication_date}"

    def get_absolute_url(self):
        return reverse("news_detail", args=[str(self.id)])

    def short_content(self):
        if len(self.content) < 200:
            return self.content
        else:
            return f"{self.content[:200]}..."

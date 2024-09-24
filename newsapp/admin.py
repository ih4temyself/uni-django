from django.contrib import admin

from newsapp.models import Author, News


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_date")
    list_filter = ("author", "publication_date")
    search_fields = ("title", "content")
    date_hierarchy = "publication_date"

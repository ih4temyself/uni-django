from django.urls import path

from newsapp import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("news/", views.NewsListView.as_view(), name="news_list"),
    path("news/<int:pk>/", views.NewsDetailView.as_view(), name="news_detail"),
    path("authors/", views.AuthorListView.as_view(), name="author_list"),
    path(
        "authors/<int:pk>/news/", views.AuthorNewsListView.as_view(), name="author_news"
    ),
    path("authors/<int:pk>/", views.AuthorDetailView.as_view(), name="author_detail"),
]

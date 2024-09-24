# newsapp/views.py

from django.views.generic import DetailView, ListView

from .models import Author, News


class HomePageView(ListView):
    model = News
    template_name = "home.html"
    context_object_name = "news_list"
    queryset = News.objects.order_by("-publication_date")[:10]


class NewsListView(ListView):
    model = News
    template_name = "news_list.html"
    context_object_name = "news_list"
    paginate_by = 10
    queryset = News.objects.order_by("-publication_date")


class NewsDetailView(DetailView):
    model = News
    template_name = "news_detail.html"
    context_object_name = "news"


class AuthorListView(ListView):
    model = Author
    template_name = "author_list.html"
    context_object_name = "authors"


class AuthorDetailView(DetailView):
    model = Author
    template_name = "author_detail.html"
    context_object_name = "author"


class AuthorNewsListView(ListView):
    model = News
    template_name = "author_news_list.html"
    context_object_name = "news_list"
    paginate_by = 10

    def get_queryset(self):
        self.author = Author.objects.get(pk=self.kwargs["pk"])
        return News.objects.filter(author=self.author).order_by("-publication_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] = self.author
        return context

from bookmarks.views import BookmarkViewSet, CategoryViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"bookmarks", BookmarkViewSet, basename="bookmark")
router.register(r"categories", CategoryViewSet, basename="category")

urlpatterns = [
    path("api/", include(router.urls)),
]

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from bookmarks.views import BookmarkViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r"bookmarks", BookmarkViewSet, basename="bookmark")
router.register(r"categories", CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
]

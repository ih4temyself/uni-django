from django.urls import path

from . import views

urlpatterns = [path("", views.christmas_checker, name="homepage")]

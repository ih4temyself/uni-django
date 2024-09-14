from django.urls import path

from . import views

urlpatterns = [path("", views.secret_santa, name="secret-santa")]

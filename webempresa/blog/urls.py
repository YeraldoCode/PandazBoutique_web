from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog, name="blog"),
]


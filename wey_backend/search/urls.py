from django.urls import path

from search.api import search

urlpatterns = [
    path("", search, name="search"),
]

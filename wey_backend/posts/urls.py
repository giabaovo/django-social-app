from django.urls import path

from posts.api import posts_list, post_create

urlpatterns = [
    path("", posts_list, name="posts_list"),
    path("create/", post_create, name="post_create"),
]

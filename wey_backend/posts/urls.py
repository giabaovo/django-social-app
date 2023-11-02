from django.urls import path

from posts.api import posts_list, post_create, posts_list_by_profile

urlpatterns = [
    path("", posts_list, name="posts_list"),
    path("profile/<uuid:id>/", posts_list_by_profile, name="posts_list_by_profile"),
    path("create/", post_create, name="post_create"),
]

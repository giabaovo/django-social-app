from rest_framework.decorators import api_view

from django.http import JsonResponse

from account.models import User
from account.serializers import UserSerializer

from posts.models import Post
from posts.serializers import PostSerializer


@api_view(["POST"])
def search(request):
    data = request.data

    query = data.get("query")

    users = User.objects.filter(name__icontains=query)
    users_serializer = UserSerializer(users, many=True)

    posts = Post.objects.filter(body__icontains=query)
    posts_serializer = PostSerializer(posts, many=True)

    return JsonResponse({"users": users_serializer.data, "posts": posts_serializer.data}, safe=False)
from rest_framework.decorators import api_view

from django.http import JsonResponse

from posts.models import Post
from posts.serializers import PostSerializer
from posts.forms import PostForm

@api_view(["GET"])
def posts_list(request):
    posts = Post.objects.all()

    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(["POST"])
def post_create(request):
    form = PostForm(request.data)

    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = request.user
        post.save()
        
        serializer = PostSerializer(post)

        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({"error": "error"})


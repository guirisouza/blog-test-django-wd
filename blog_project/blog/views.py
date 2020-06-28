from django.shortcuts import render

from .models import Post


def post_list_view(request):
    queryset = Post.objects.all()
    context = {
        "posts_view": queryset
    }



from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Post


def post_list_view(request):
    queryset = Post.objects.all()
    template_name = "home.html"
    context = {
        "posts_view": queryset,
        "title": "Home"
    }
    return render(request, template_name, context)

def post_detail_view(request, slug):
    post_object = get_object_or_404(Post, slug=slug)
    template_name = "post-detail.html"
    context = {
        "post": post_object
    }
    return render(request, template_name, context)



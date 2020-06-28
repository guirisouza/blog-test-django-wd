from django.shortcuts import render

from .models import Post


def post_list_view(request):
    queryset = Post.objects.all()
    template_name = "home.html"
    context = {
        "posts_view": queryset,
        "title": "Home"
    }
    return render(request, template_name, context)



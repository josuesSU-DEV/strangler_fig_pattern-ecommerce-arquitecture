from django.shortcuts import render
from blog.models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, publicacion_id):
    post = Post.objects.get(pk=publicacion_id)
    return render(request, "blog/post_detail.html", {"post": post})

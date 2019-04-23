from django.shortcuts import render

from .models import Post


def index(request):
    posts = Post.objects.all()[:5]
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)


def show(request, id):
    post = Post.objects.get(pk=id)
    context = {
        'post': post
    }
    return render(request, 'show.html', context)
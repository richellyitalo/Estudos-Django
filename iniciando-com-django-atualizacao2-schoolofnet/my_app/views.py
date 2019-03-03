from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category


def home(request):
    return HttpResponse('Página inicial')


def posts(request):
    categories = Category.objects.all()

    if 'category_id' in request.GET:
        category_id = request.GET['category_id']
        #category = Category.objects.get(id=category_id)
        #posts = Post.objects.filter(categories=category)
        posts = Post.objects.filter(categories=category_id)
    else:
        posts = Post.objects.all()
    context = {
        'posts': posts,
        'categories': categories
    }
    return render(request, 'posts.html', context)


def posts_single(request, post_id):
    categories = Category.objects.all()
    post = Post.objects.get(id=post_id)
    context = {
        'post': post,
        'categories': categories
    }
    return render(request, 'post.html', context)

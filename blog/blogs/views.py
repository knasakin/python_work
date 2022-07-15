from django.shortcuts import render, redirect
from .forms import *
from .models import *


def index(request):
    return render(request, 'blogs/index.html')


def render_posts(request):

    posts = BlogPost.objects.all()
    context = {'posts': posts}

    return render(request, 'blogs/posts.html', context=context)


def render_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    context = {'post': post}

    return render(request, 'blogs/post.html', context=context)


def create_new_post(request):
    if request.method != 'POST':  # создаём пустую форму, т.к. данные не отправлялись
        form = BlogPostForm()
    else:  # обрабатываем отправленные данные
        form = BlogPostForm(data=request.POST)

        if form.is_valid():
            form.save()

        return redirect('blogs:posts')  # редирект на posts/

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context=context)


def edit_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)

    if request.method != 'POST':
        form = BlogPostForm(instance=post)  # создаём форму, заполненную информацией из существующего объекта записи

    else:
        form = BlogPostForm(instance=post, data=request.POST)  # создаём форму с обновлёнными данными из request.POST

        if form.is_valid():
            form.save()

            return redirect('blogs:post', post_id=post.id)

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import *
from .models import *


def index(request):
    return render(request, 'blogs/index.html')


@login_required
def render_posts(request):
    posts = BlogPost.objects.filter(owner=request.user)

    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context=context)


@login_required
def render_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    check_topic_owner(request.user, post.owner)

    context = {'post': post}
    return render(request, 'blogs/post.html', context=context)


@login_required
def add_new_post(request):
    if request.method != 'POST':  # создаём пустую форму, т.к. данные не отправлялись
        form = BlogPostForm()

    else:  # обрабатываем отправленные данные
        form = BlogPostForm(data=request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()

        return redirect('blogs:posts')  # редирект на posts/

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context=context)


@login_required
def edit_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    check_topic_owner(request.user, post.owner)

    if request.method != 'POST':
        form = BlogPostForm(instance=post)  # создаём форму, заполненную информацией из существующего объекта записи

    else:
        form = BlogPostForm(instance=post, data=request.POST)  # создаём форму с обновлёнными данными из request.POST

        if form.is_valid():
            form.save()

            return redirect('blogs:post', post_id=post.id)

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)


def check_topic_owner(user, owner):
    """Сравнивает текущего пользователя с владельцем записи"""

    if user != owner:
        print('разные юзеры')
        raise Http404
    print('юзеры равны')

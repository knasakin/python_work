from django.urls import path
from .views import *


app_name = 'blogs'  # в шаблоне пишу {% url 'blogs:index' %} вместо {% url 'index' %}

urlpatterns = [
    path('', index, name='index'),
    path('posts/', render_posts, name='posts'),
    path('new_post/', add_new_post, name='new_post'),
    path('post/<int:post_id>/', render_post, name='post'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post')
]

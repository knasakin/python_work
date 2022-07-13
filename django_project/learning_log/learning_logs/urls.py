"""Определяет схемы URL для learning_logs."""
from django.urls import path
from .views import *


app_name = 'learning_logs'

urlpatterns = [
    path('', index, name='index'),
    path('topics', render_topics, name='topics'),
    path('topics/<int:topic_id>/', render_topic, name='topic'),
    path('new_topic/', render_new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', render_new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', edit_entry, name='edit_entry'),
]

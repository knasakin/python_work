"""Определяет схемы URL для пользователей"""

from django.urls import path, include
from .views import *


app_name = 'users'  # пространство имён приложения users

urlpatterns = [
    path('', include('django.contrib.auth.urls')),  # по умолчанию включают именованные схемы 'login' и 'logout'
    path('register/', register, name='register'),
]

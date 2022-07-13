from django.urls import path
from .views import *


app_name = 'meal_plans'

urlpatterns = [
    path('', index, name='index'),
]

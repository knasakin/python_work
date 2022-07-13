from django.urls import path
from .views import *


app_name = 'pizzas'

urlpatterns = [
    path('', index, name='index'),
    path('pizzas', render_pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>/', render_pizza, name='pizza')
]

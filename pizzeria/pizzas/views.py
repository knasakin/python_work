from django.shortcuts import render
from .models import *


def index(request):
    """Домашняя страница приложения Pizzeria"""

    return render(request, 'pizzas/posts.html')


def render_pizzas(request):
    """Выводит список пицц"""

    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}

    return render(request, 'pizzas/pizzas.html', context=context)


def render_pizza(request, pizza_id):
    """Выводит пиццу по идентификатору и весь её состав"""

    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {'pizza': pizza, 'toppings': toppings}

    return render(request, 'pizzas/pizza.html', context=context)

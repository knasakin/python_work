from django.db import models


class Pizza(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=200)

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)  # внешний ключ

    class Meta:
        verbose_name_plural = 'toppings'  # форма множественного числа для модели Topping

    def __str__(self):
        return self.name

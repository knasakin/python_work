from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Регистрирует нового пользователя."""

    if request.method != 'POST':
        form = UserCreationForm()  # Выводим пустую форму регистрации

    else:
        form = UserCreationForm(data=request.POST)  # Обработка заполненной формы

        if form.is_valid():
            new_user = form.save()  # сохраняем имя пользователя и хеша пароля в БД
            login(request, new_user)  # логинимся

            return redirect('blogs:index')  # перенаправление на домашнюю страницу

    context = {'form': form}
    return render(request, 'registration/register.html', context)  # выводим пустую или недействительную форму

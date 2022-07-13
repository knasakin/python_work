from django.shortcuts import render, redirect
from .forms import TopicForm, EntryForm
from .models import *


def index(request):
    """Домашняя страница приложения Learning Log"""

    return render(request, 'learning_logs/index.html')


def render_topics(request):
    """Выводит список тем."""

    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}

    return render(request, 'learning_logs/topics.html', context=context)


def render_topic(request, topic_id):
    """Выводит одну тему и все ее записи."""

    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}

    return render(request, 'learning_logs/topic.html', context=context)


def render_new_topic(request):
    """Определяет новую тему."""

    if request.method != 'POST':  # создаём пустую форму, т.к. данные не отправлялись
        form = TopicForm()

    else:  # обрабатываем отправленные данные
        form = TopicForm(data=request.POST)

        if form.is_valid():
            form.save()

            return redirect('learning_logs:topics')  # редирект на topics/

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context=context)


def render_new_entry(request, topic_id):
    """Добавляет новую запись по конкретной теме."""

    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':  # создаём пустую форму, т.к. данные не отправлялись
        form = EntryForm()

    else:  # обрабатываем отправленные данные
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)  # commit=False - не сохраняем в БД
            new_entry.topic = topic
            new_entry.save()

            return redirect('learning_logs:topic', topic_id=topic_id)  # редирект на topic/topic_id/

    context = {'form': form, 'topic': topic}
    return render(request, 'learning_logs/new_entry.html', context=context)


def edit_entry(request, entry_id):
    """Редактирует существующую запись."""

    entry = Entry.objects.get(id=entry_id)  # получаем объект записи для редактирования
    topic = entry.topic  # получаем тему, связанную с этой записью

    if request.method != 'POST':  # Исходный запрос; форма заполняется данными текущей записи
        form = EntryForm(instance=entry)  # создаём форму, заполненную информацией из существующего объекта записи

    else:  # обрабатываем отправленные данные
        form = EntryForm(instance=entry, data=request.POST)  # создаём форму с обновлёнными данными из request.POST

        if form.is_valid():
            form.save()

            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

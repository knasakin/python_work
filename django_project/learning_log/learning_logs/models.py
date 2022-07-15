from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """Тема, которую изучает пользователь"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # внешний ключ к таблице User

    def __str__(self):
        """Возвращает строковое представление модели."""

        return self.text


class Entry(models.Model):
    """Информация, изученная пользователем по теме"""

    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # внешний ключ к таблице Topic

    class Meta:
        verbose_name_plural = 'entries'  # форма множественного числа для модели Entry

    def __str__(self):
        """Возвращает строковое представление модели."""

        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text

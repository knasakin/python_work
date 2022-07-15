from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'posts'  # форма множественного числа для модели Entry

    def __str__(self):
        return self.title

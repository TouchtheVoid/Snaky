from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    priority = models.IntegerField(default=1, verbose_name='Приоритет')
    deadline = models.DateField(verbose_name='Срок выполнения')
    completed = models.BooleanField(default=False, verbose_name='Завершено')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


    def __str__(self):
        return self.title
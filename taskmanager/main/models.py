from django.db import models


class Task(models.Model):
    title = models.CharField('Назвние', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'записи'
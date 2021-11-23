from django.db import models


class Task(models.Model):
    title = models.CharField('Назвние', max_length=50)
    task = models.TextField('Описание')
    time = models.DateTimeField('Время сосздание поста', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'записи'
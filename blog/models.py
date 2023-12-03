from django.db import models
from django.utils import timezone

from newsletter.models import NULLABLE


# Create your models here.


class Blog(models.Model):
    header = models.CharField(max_length=150, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(verbose_name='Изображение', **NULLABLE)
    count_view = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    data_publication = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.header

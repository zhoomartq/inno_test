from django.utils import timezone
from django.db import models
from django.db.models import DateField


class Document(models.Model):
    rubrics = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField()
    created_date = DateField(default=timezone.now, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        ordering = ('-created_date',)

    def __str__(self):
        return self.rubrics

from django.db import models

# Create your models here.
from django.db import models


class ServiceCategory(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', blank=True)
    icon = models.CharField('Иконка', max_length=50, default='settings')
    order = models.IntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активна', default=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Категория услуг'
        verbose_name_plural = 'Категории услуг'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE,
                                 related_name='services', verbose_name='Категория')
    name = models.CharField('Название услуги', max_length=200)
    description = models.TextField('Описание')
    price_from = models.DecimalField('Цена от', max_digits=10, decimal_places=2)
    duration = models.CharField('Срок выполнения', max_length=100)
    image = models.ImageField('Изображение', upload_to='services/', blank=True, null=True)
    is_popular = models.BooleanField('Популярная', default=False)
    is_active = models.BooleanField('Активна', default=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['-is_popular', 'name']

    def __str__(self):
        return self.name
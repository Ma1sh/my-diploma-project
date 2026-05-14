from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings


class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В работе'),
        ('waiting_parts', 'Ожидание запчастей'),
        ('ready', 'Готова'),
        ('completed', 'Завершена'),
        ('cancelled', 'Отменена'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий'),
        ('urgent', 'Срочный'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='orders', verbose_name='Клиент')
    service = models.ForeignKey('services.Service', on_delete=models.SET_NULL,
                                null=True, verbose_name='Услуга')

    # Информация о заказе
    title = models.CharField('Название заказа', max_length=200)
    description = models.TextField('Описание проблемы')
    device_type = models.CharField('Тип устройства', max_length=100)
    device_model = models.CharField('Модель устройства', max_length=100, blank=True)

    # Статус и приоритет
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='new')
    priority = models.CharField('Приоритет', max_length=20, choices=PRIORITY_CHOICES, default='medium')

    # Контактная информация
    contact_phone = models.CharField('Контактный телефон', max_length=20)
    contact_email = models.EmailField('Email для связи', blank=True)

    # Стоимость и сроки
    estimated_cost = models.DecimalField('Предварительная стоимость', max_digits=10,
                                         decimal_places=2, null=True, blank=True)
    final_cost = models.DecimalField('Итоговая стоимость', max_digits=10,
                                     decimal_places=2, null=True, blank=True)
    estimated_date = models.DateField('Предполагаемая дата готовности', null=True, blank=True)

    # Комментарии и заметки
    admin_notes = models.TextField('Заметки администратора', blank=True)
    client_notes = models.TextField('Комментарий клиента', blank=True)

    # Даты
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    completed_at = models.DateTimeField('Дата завершения', null=True, blank=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']

    def __str__(self):
        return f"Заказ #{self.id} - {self.title}"


class OrderStatusHistory(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name='status_history', verbose_name='Заказ')
    status = models.CharField('Статус', max_length=20)
    comment = models.TextField('Комментарий', blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                   null=True, verbose_name='Изменил')
    created_at = models.DateTimeField('Дата изменения', auto_now_add=True)

    class Meta:
        verbose_name = 'История статуса'
        verbose_name_plural = 'История статусов'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.order} - {self.status}"
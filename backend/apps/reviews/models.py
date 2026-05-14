from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='reviews', verbose_name='Автор')
    order = models.ForeignKey('orders.Order', on_delete=models.SET_NULL,
                              null=True, blank=True, related_name='reviews',
                              verbose_name='Заказ')

    rating = models.IntegerField('Оценка', validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.TextField('Текст отзыва')

    is_approved = models.BooleanField('Одобрен', default=False)
    is_featured = models.BooleanField('Рекомендуемый', default=False)

    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

    def __str__(self):
        return f"Отзыв от {self.user.get_full_name()} - {self.rating}/5"
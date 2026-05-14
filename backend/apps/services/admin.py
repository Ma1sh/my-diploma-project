from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ServiceCategory, Service


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'description')
    list_editable = ('order', 'is_active')
    ordering = ('order', 'name')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price_from', 'duration',
                    'is_popular', 'is_active', 'created_at')
    list_filter = ('category', 'is_popular', 'is_active', 'created_at')
    search_fields = ('name', 'description')
    list_editable = ('is_popular', 'is_active')
    ordering = ('-created_at',)

    fieldsets = (
        ('Основная информация', {
            'fields': ('category', 'name', 'description')
        }),
        ('Цены и сроки', {
            'fields': ('price_from', 'duration')
        }),
        ('Медиа', {
            'fields': ('image',)
        }),
        ('Настройки', {
            'fields': ('is_popular', 'is_active')
        }),
    )
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'is_approved', 'is_featured', 'created_at')
    list_filter = ('rating', 'is_approved', 'is_featured', 'created_at')
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'text')
    list_editable = ('is_approved', 'is_featured')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Информация об отзыве', {
            'fields': ('user', 'order', 'rating', 'text')
        }),
        ('Модерация', {
            'fields': ('is_approved', 'is_featured')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
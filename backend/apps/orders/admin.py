from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Order, OrderStatusHistory


class OrderStatusHistoryInline(admin.TabularInline):
    model = OrderStatusHistory
    extra = 0
    readonly_fields = ('created_at', 'created_by')
    can_delete = False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'service', 'status', 'priority',
                    'created_at', 'estimated_date')
    list_filter = ('status', 'priority', 'service__category', 'created_at')
    search_fields = ('title', 'description', 'device_type', 'device_model',
                     'user__email', 'contact_phone')
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at', 'updated_at', 'completed_at')
    inlines = [OrderStatusHistoryInline]

    fieldsets = (
        ('Основная информация', {
            'fields': ('user', 'service', 'title', 'description')
        }),
        ('Устройство', {
            'fields': ('device_type', 'device_model')
        }),
        ('Статус и приоритет', {
            'fields': ('status', 'priority')
        }),
        ('Контакты', {
            'fields': ('contact_phone', 'contact_email')
        }),
        ('Стоимость и сроки', {
            'fields': ('estimated_cost', 'final_cost', 'estimated_date')
        }),
        ('Комментарии', {
            'fields': ('client_notes', 'admin_notes')
        }),
        ('Системная информация', {
            'fields': ('created_at', 'updated_at', 'completed_at'),
            'classes': ('collapse',)
        }),
    )

    def save_model(self, request, obj, form, change):
        if change and 'status' in form.changed_data:
            OrderStatusHistory.objects.create(
                order=obj,
                status=obj.status,
                comment=f'Статус изменен администратором',
                created_by=request.user
            )
        super().save_model(request, obj, form, change)


@admin.register(OrderStatusHistory)
class OrderStatusHistoryAdmin(admin.ModelAdmin):
    list_display = ('order', 'status', 'created_by', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('order__title', 'comment')
    readonly_fields = ('created_at',)
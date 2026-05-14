from rest_framework import serializers
from .models import Order, OrderStatusHistory
from apps.users.serializers import UserSerializer
from apps.services.serializers import ServiceListSerializer


class OrderStatusHistorySerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.get_full_name', read_only=True)

    class Meta:
        model = OrderStatusHistory
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    user_info = UserSerializer(source='user', read_only=True)
    service_info = ServiceListSerializer(source='service', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    priority_display = serializers.CharField(source='get_priority_display', read_only=True)
    status_history = OrderStatusHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('user', 'created_at', 'updated_at', 'completed_at')


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('service', 'title', 'description', 'device_type', 'device_model',
                  'contact_phone', 'contact_email', 'client_notes')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class OrderListSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source='service.name', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'title', 'service_name', 'status', 'status_display',
                  'priority', 'created_at', 'estimated_date')
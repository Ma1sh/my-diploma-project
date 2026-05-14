from rest_framework import serializers
from .models import ServiceCategory, Service


class ServiceCategorySerializer(serializers.ModelSerializer):
    services_count = serializers.SerializerMethodField()

    class Meta:
        model = ServiceCategory
        fields = '__all__'

    def get_services_count(self, obj):
        return obj.services.filter(is_active=True).count()


class ServiceSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Service
        fields = '__all__'


class ServiceListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Service
        fields = ('id', 'name', 'price_from', 'duration', 'image',
                  'is_popular', 'category_name')
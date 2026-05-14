from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import ServiceCategory, Service
from .serializers import (ServiceCategorySerializer, ServiceSerializer,
                          ServiceListSerializer)


class ServiceCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServiceCategory.objects.filter(is_active=True)
    serializer_class = ServiceCategorySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['order', 'name']


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.filter(is_active=True)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'is_popular']
    search_fields = ['name', 'description']
    ordering_fields = ['price_from', 'created_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return ServiceListSerializer
        return ServiceSerializer
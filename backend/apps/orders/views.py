from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Order, OrderStatusHistory
from .serializers import (OrderSerializer, OrderCreateSerializer,
                          OrderListSerializer, OrderStatusHistorySerializer)


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'priority', 'service']
    search_fields = ['title', 'description', 'device_type']
    ordering_fields = ['created_at', 'updated_at', 'priority']

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        elif self.action == 'list':
            return OrderListSerializer
        return OrderSerializer

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
    def change_status(self, request, pk=None):
        order = self.get_object()
        new_status = request.data.get('status')
        comment = request.data.get('comment', '')

        if new_status not in dict(Order.STATUS_CHOICES):
            return Response({'error': 'Неверный статус'},
                            status=status.HTTP_400_BAD_REQUEST)

        old_status = order.status
        order.status = new_status
        order.save()

        OrderStatusHistory.objects.create(
            order=order,
            status=new_status,
            comment=comment,
            created_by=request.user
        )

        return Response({'status': 'Статус изменен', 'old_status': old_status,
                         'new_status': new_status})
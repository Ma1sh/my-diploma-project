from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Review
from .serializers import ReviewSerializer, ReviewCreateSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['rating', 'is_featured']
    ordering_fields = ['created_at', 'rating']

    def get_queryset(self):
        if self.request.user.is_staff:
            return Review.objects.all()
        elif self.request.user.is_authenticated:
            return Review.objects.filter(is_approved=True) | Review.objects.filter(user=self.request.user)
        return Review.objects.filter(is_approved=True)

    def get_serializer_class(self):
        if self.action == 'create':
            return ReviewCreateSerializer
        return ReviewSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [permissions.IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

    @action(detail=False, methods=['get'])
    def featured(self, request):
        featured_reviews = Review.objects.filter(is_approved=True, is_featured=True)[:6]
        serializer = self.get_serializer(featured_reviews, many=True)
        return Response(serializer.data)
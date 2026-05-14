from rest_framework import serializers
from .models import Review
from apps.users.serializers import UserSerializer


class ReviewSerializer(serializers.ModelSerializer):
    user_info = UserSerializer(source='user', read_only=True)
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'is_approved', 'is_featured', 'created_at', 'updated_at')


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('order', 'rating', 'text')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
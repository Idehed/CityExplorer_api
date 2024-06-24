from rest_framework import serializers
from .models import Guide

class GuideSerializer(serializers.ModelSerializer):
    """
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    reviews_count = serializers.ReadOnlyField()
    average_rating = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """
        """
        model = Guide
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'profile_image', 'city', 'duration', 'cost',
            'email', 'phone', 'created_at', 'updated_at',
            'reviews_count', 'average_rating',
        ]
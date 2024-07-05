from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contact model
    """
    class Meta:
        model = Contact
        fields = ['id', 'name', 'topic', 'email', 'message', 'created_at']

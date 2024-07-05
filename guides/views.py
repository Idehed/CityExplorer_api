from django.db.models import Count, Avg
from rest_framework import generics, permissions, filters
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Guide
from .serializers import GuideSerializer

class GuideList(generics.ListCreateAPIView):
    """
    List all the comments or create one if you are logged in 
    calculate the number of reviews and an average rating number
    """
    serializer_class = GuideSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Guide.objects.annotate(
        reviews_count=Count('reviews', distinct=True),
        average_rating=Avg('reviews__rating')
    ).order_by('-created_at')

    filter_backends = [
        filters.SearchFilter
    ]

    search_fields = [
        'owner__username',
        'city'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class GuideDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = GuideSerializer
    queryset = Guide.objects.annotate(
        reviews_count=Count('reviews', distinct=True),
        average_rating=Avg('reviews__rating')
    ).order_by('-created_at')

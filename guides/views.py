from rest_framework import generics, permissions, filters
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Guide
from .serializers import GuideSerializer

class GuideList(generics.ListCreateAPIView):
    """
    """
    serializer_class = GuideSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Guide.objects.all()

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
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = GuideSerializer
    queryset = Guide.objects.all().order_by('-created_at')

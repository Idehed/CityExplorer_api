from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewDetailSerializer, ReviewSerializer


class ReviewList(generics.ListCreateAPIView):
    """
    List all the reviews and create a review if you are logged in
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['guide']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a review, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReviewDetailSerializer
    queryset = Review.objects.all()

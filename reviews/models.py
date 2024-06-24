from django.db import models
from django.contrib.auth.models import User
from guides.models import Guide

class Review(models.Model):
    """
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    guide = models.ForeignKey(
        Guide, on_delete=models.CASCADE, related_name='reviews'
    )
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.owner}' review"

from django.db import models
from django.contrib.auth.models import User


class Guide(models.Model):
    """
    Guides model, related to user
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Ordering with the lastest first
        """
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.owner}'s Guide Details"

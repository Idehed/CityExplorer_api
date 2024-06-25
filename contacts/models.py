from django.db import models


class Contact(models.Model):
    """
    Model to handle the contact form submissions
    """

    name = models.CharField(max_length=200)
    topic = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=700)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"From {self.name} : {self.topic}"
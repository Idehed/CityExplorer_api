from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('name', 'topic', 'email', 'created_at')
    list_filter = ('created_at',)
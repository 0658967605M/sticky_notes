"""
admin.py

Registers stick notes models to the Django admin interface,
allowing CRUD operations through the admin panel.
"""

from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

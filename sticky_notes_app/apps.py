"""
app.py

Configuration for the stick_notes application. This file
defines the app name and any app-specific settings.
"""

from django.apps import AppConfig

class StickyNotesAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sticky_notes_app'

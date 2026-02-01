"""
models.py

Defines database models for the stick_notes application.
Each model represents a database table and its fields.
"""

from django.db import models

class Note(models.Model):
    """
    Model representing a single sticky note.

    Attributes:
        title (str): Title of the note.
        content (str): Text content of the note.
        created_at (datetime): Timestamp when the note was created.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Return the string representation of the note.
        """
        return self.title

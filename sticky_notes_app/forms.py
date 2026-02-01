"""
forms.py

Contains Django forms used for creating and updating sticky notes.
These forms handle validation and rendering of HTML input fields.
"""

from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']

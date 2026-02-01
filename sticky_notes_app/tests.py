"""
tests.py

Contains unit tests for the Sticky Notes application.
These tests verify that note creation, listing, updating,
and deletion work as expected.
"""

from django.test import TestCase
from django.urls import reverse
from .models import Note


class NoteTests(TestCase):
    """
    Test suite for the Note model and related views.
    """

    def setUp(self):
        """
        Set up test data before each test runs.
        Creates a sample note used across multiple tests.
        """
        self.note = Note.objects.create(
            title="Test Note",
            content="Test Content"
        )

    def test_note_list_view(self):
        """
        Test that the note list view loads successfully
        and displays existing notes.
        """
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_note_create(self):
        """
        Test that a new note can be created via POST request.
        """
        response = self.client.post(
            reverse('note_create'),
            {
                'title': 'New Note',
                'content': 'New Content'
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 2)

    def test_note_update(self):
        """
        Test that an existing note can be updated.
        """
        response = self.client.post(
            reverse('note_update', args=[self.note.id]),
            {
                'title': 'Updated Title',
                'content': 'Updated Content'
            }
        )
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Title')

    def test_note_delete(self):
        """
        Test that a note can be deleted.
        """
        response = self.client.get(
            reverse('note_delete', args=[self.note.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 0)

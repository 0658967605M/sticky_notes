"""
views.py

Handles HTTP requests for the Sticky Notes application.
Includes views for listing, creating, updating, and deleting notes.
"""

from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm


def home(request):
    """
    Display the home page with all sticky notes ordered by creation date.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered home page with notes.
    """
    notes = Note.objects.all().order_by("-created_at")
    return render(request, "sticky_notes_app/home.html", {"notes": notes})


def note_create(request):
    """
    Handle creation of a new sticky note.

    Args:
        request (HttpRequest): The HTTP request containing form data.

    Returns:
        HttpResponse: Redirects to note list on success or displays the form.
    """
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm()

    return render(request, "sticky_notes_app/note_form.html", {"form": form})


def note_list(request):
    """
    Display a list of all sticky notes.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered page showing all notes.
    """
    notes = Note.objects.all()
    return render(
        request,
        "sticky_notes_app/note_list.html",
        {"notes": notes}
    )


def note_update(request, id):
    """
    Update an existing sticky note.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the note to update.

    Returns:
        HttpResponse: Redirects to note list after update or shows update form.
    """
    note = get_object_or_404(Note, id=id)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)

    return render(
        request,
        'sticky_notes_app/note_update.html',
        {'form': form}
    )


def note_delete(request, id):
    """
    Delete a sticky note.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the note to delete.

    Returns:
        HttpResponse: Redirects to the note list after deletion.
    """
    note = get_object_or_404(Note, id=id)
    note.delete()
    return redirect('note_list')

from notes_app.views import NotesView, EditNote, CreateNote, DeleteNote, NoteDetailView
from django.urls import path

from notes_app import views

app_name = "notes"

urlpatterns = [
    path("", NotesView.as_view(), name="index"),
    path("note_detail/<pk>/", NoteDetailView.as_view(), name="note_detail"),
    path("create-note/", CreateNote.as_view(), name="create"),
    path("edit-note/<slug:pk>/", EditNote.as_view(), name="edit"),
    path("delete-note/<slug:pk>/", DeleteNote.as_view(), name="delete"),
]

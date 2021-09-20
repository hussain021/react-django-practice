from notes_app.views import DeleteNote, NotesDetail, EditNote, EditOrDeleteNote, CreateNote
from django.urls import path

app_name = 'notes'

urlpatterns = [
    path('', NotesDetail.as_view(), name='index'),
    path('create-note/', CreateNote.as_view(), name='create'),
    path('delete-note/', DeleteNote.as_view(), name='delete'),
    path('edit-note/', EditNote.as_view(), name='edit'),
    path('edit-or-delete-note/', EditOrDeleteNote.as_view(), name='edit_or_delete')
]

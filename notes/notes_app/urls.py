from django.urls import path

from . import views

urlpatterns = [
    path('', views.notes_details, name='index'),
    path('create_note/', views.create_note, name='create'),
    path('delete_note/', views.delete_note, name='delete'),
    path('edit_note/', views.edit_note, name='edit'),
    path('edit_or_delete_note/', views.edit_or_delete, name='edit_or_delete')
]

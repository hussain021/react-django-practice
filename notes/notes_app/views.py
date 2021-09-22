from django.http import request
from notes_app.forms import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q
from django.shortcuts import redirect, render, reverse
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from notes_app.constants import PRIVATE, PUBLIC
from notes_app.forms import NotesUserCreationForm
from notes_app.models import Note


class SignUpView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = NotesUserCreationForm

    def get_success_url(self):
        return reverse("/login")


class EditProfile(UpdateView):
    template_name = "registration/edit_profile.html"
    model = User
    success_url = "/login"

    def get_form(self, form_class=None):
        form = PasswordChangeForm(self.request.user, self.request.POST)
        return form

    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)
        messages.success(self.request, "Your password was successfully updated!")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("form invalid")
        messages.error(self.request, "Please correct the error below.")
        return super().form_invalid(form)


class NotesView(ListView):
    model = Note
    template_name = "notes_app/all_notes.html"
    context_object_name = "notes"

    def get_queryset(self):
        queryset = {
            "public_notes": Note.objects.filter(
                Q(visibility="PB") & ~Q(created_by=self.request.user.id)
            ),
            "my_notes": Note.objects.filter(created_by=self.request.user.id),
        }
        return queryset


class NoteDetailView(DetailView):
    model = Note
    template_name = "notes_app/note_detail.html"
    context_object_name = "note"


class CreateNote(CreateView):
    template_name = "notes_app/notes_create.html"
    success_url = "/"
    model = Note
    fields = ["note_title", "note_text", "visibility"]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class EditNote(UpdateView):
    template_name = "notes_app/notes_create.html"
    success_url = "/"
    model = Note
    fields = ["note_title", "note_text", "visibility"]


class DeleteNote(DeleteView):
    template_name = "notes_app/notes_delete.html"
    success_url = "/"
    model = Note
    fields = ["note_title", "note_text", "visibility"]

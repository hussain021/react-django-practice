from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

from notes_app.models import Note


User = get_user_model()


class DateInput(forms.DateInput):
    input_type = "date"


class NotesModelForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("note_title", "note_text", "visibility")


class NotesUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = {
            "username",
        }
        field_classes = {"username": UsernameField}

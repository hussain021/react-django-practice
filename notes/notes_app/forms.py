from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.db.models import fields

User = get_user_model()


class DateInput(forms.DateInput):
    input_type = "date"


class NoteForm(forms.Form):
    note_title = forms.CharField(max_length=30)
    note_text = forms.CharField(max_length=150)
    visibility = forms.BooleanField(required=False)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = {
            "username",
        }
        field_classes = {"username": UsernameField}

from django.contrib.auth import get_user_model
from django.db.models import fields
from .models import Note
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()

class DateInput(forms.DateInput):
    input_type = 'date'

class NoteForm(forms.Form):
    note_title = forms.CharField(max_length=30)
    note_text = forms.CharField(max_length=150)
    visibility = forms.BooleanField(required=False)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = {"username",}
        field_classes = {'username': UsernameField}

"""class NoteEditForm(forms.Form):

    def __init__(self, *args, **kwargs):
           super(BuyForm, self).__init__(*args, **kwargs)
       self.fields['buyer'].required = False
       self.fields['buyer'].widget.attrs['disabled'] = "disabled" 

       ...

    def clean_buyer(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.buyer
        else:
            return self.cleaned_data.get('buyer', None)

    id = forms.IntegerField()
    note_text = forms.CharField()"""
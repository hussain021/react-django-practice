from datetime import date
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q
from django.shortcuts import redirect, render, reverse
from django.views import generic
from django.views.generic.base import View

from notes_app.constants import PRIVATE, PUBLIC
from notes_app.forms import NotesUserCreationForm, NotesModelForm
from notes_app.models import Note



class SignUpView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = NotesUserCreationForm

    def get_success_url(self):
        return reverse("/login")


class EditProfile(View):
    template_name = "registration/edit_profile.html"

    def get(self, request):
        if request.user.is_authenticated:
            form = PasswordChangeForm(request.user)
            return render(request, self.template_name, {"form": form})
        else:
            return redirect("/login")

    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, "Your password was successfully updated!")
            return redirect("notes:index")
        else:
            messages.error(request, "Please correct the error below.")


class NotesDetail(View):
    def get(self, request):
        public_notes = Note.objects.filter(
            Q(visibility="PB") & ~Q(created_by=request.user.id)
        )
        if request.user.is_authenticated:
            my_notes = Note.objects.filter(created_by=request.user.id)
            context = {"my_notes": my_notes, "public_notes": public_notes}
            return render(request, "notes_app/notes_details.html", context)
        else:
            context = {"my_notes": {}, "public_notes": public_notes}
            return render(request, "notes_app/notes_details.html", context)


class CreateNote(View):
    def post(self, request):
        if request.user.is_authenticated:
            form = NotesModelForm(request.POST)
            if form.is_valid():
                note = form.save(commit=False)
                note.created_by = request.user
                note.save()
                return redirect("notes:index")
            else:
                messages.error(request, "Please correct the error below.")
        else:
            context = {"message": "Please login/Signup to create a note!"}
            print(context)
            return redirect("/login")

    def get(self, request):
        context = {"form": NotesModelForm()}
        return render(request, "notes_app/notes_create.html", context)


class DeleteNote(View):
    def get(self, request):
        items_to_delete = request.POST.getlist("delete_items")
        Note.objects.filter(pk__in=items_to_delete).delete()
        return redirect("/notes_app")


class EditNote(View):
    def post(self, request):
        if request.method == "POST":
            note = Note.objects.get(pk=request.POST.get("id"))
            note.note_text = request.POST.get("note_text")
            note.note_title = request.POST.get("note_title")
            print(request.POST.get("visibility"))
            if request.POST.get("visibility") == "public":
                note.visibility = PUBLIC
            else:
                note.visibility = PRIVATE
            note.save()
        return redirect("notes:index")


class EditOrDeleteNote(View):
    def post(self, request):
        if request.POST.get("delete_items") is not None:
            # Fetch list of items to delete, by ID
            items_to_delete = request.POST.getlist("delete_items")
            # Delete those items all in one go
            Note.objects.filter(pk__in=items_to_delete).delete()
            return redirect("notes:index")

        else:
            note_to_edit = request.POST.getlist("edit_items")
            print(
                Note.objects.filter(pk__in=note_to_edit).values("visibility")[0][
                    "visibility"
                ]
            )
            context = {
                "note_title": Note.objects.filter(pk__in=note_to_edit).values(
                    "note_title"
                )[0]["note_title"],
                "id": Note.objects.filter(pk__in=note_to_edit).values("id")[0]["id"],
                "note_text": str(
                    Note.objects.filter(pk__in=note_to_edit).values("note_text")[0][
                        "note_text"
                    ]
                ),
                "visibility": str(
                    Note.objects.filter(pk__in=note_to_edit).values("visibility")[0][
                        "visibility"
                    ]
                ),
            }
            return render(request, "notes_app/notes_edit.html", context)

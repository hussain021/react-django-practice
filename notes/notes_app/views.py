from datetime import date
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q
from django.shortcuts import redirect, render, reverse
from django.views import generic

from .forms import CustomUserCreationForm, NoteForm
from .models import Note


class SignUpView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, "Your password was successfully updated!")
                return redirect("index")
            else:
                messages.error(request, "Please correct the error below.")
        else:
            form = PasswordChangeForm(request.user)
        return render(request, "registration/edit_profile.html", {"form": form})
    else:
        return redirect("/login")


def notes_details(request):
    public_notes = Note.objects.filter(
        Q(visibility=True) & ~Q(created_by=request.user.id)
    )
    if request.user.is_authenticated:
        my_notes = Note.objects.filter(created_by=request.user.id)
        context = {"my_notes": my_notes, "public_notes": public_notes}
        return render(request, "notes_app/notes_details.html", context)
    else:
        context = {"my_notes": {}, "public_notes": public_notes}
        return render(request, "notes_app/notes_details.html", context)


def create_note(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = NoteForm(request.POST)
            if form.is_valid():
                note_title = form.cleaned_data["note_title"]
                note_text = form.cleaned_data["note_text"]
                visibility = form.cleaned_data["visibility"]
                created_by = request.user
                created_date = date.today()
                Note.objects.create(
                    note_title=note_title,
                    note_text=note_text,
                    visibility=visibility,
                    created_by=created_by,
                    created_date=created_date,
                )
                return redirect("index")
        context = {"form": NoteForm()}
        return render(request, "notes_app/notes_create.html", context)
    else:
        context = {"message": "Please login/Signup to create a note!"}
        print(context)
        return redirect("/login")


def delete_note(request):
    if request.method == "POST":
        # Fetch list of items to delete, by ID
        items_to_delete = request.POST.getlist("delete_items")
        # Delete those items all in one go
        Note.objects.filter(pk__in=items_to_delete).delete()

    return redirect("/notes_app")


def edit_note(request):
    if request.method == "POST":
        note = Note.objects.get(pk=request.POST.get("id"))
        note.note_text = request.POST.get("note_text")
        note.note_title = request.POST.get("note_title")
        print(request.POST.get("visibility"))
        if request.POST.get("visibility") is None:
            note.visibility = False
        else:
            note.visibility = request.POST.get("visibility")
        note.save()
    return redirect("index")


def edit_or_delete(request):
    if request.method == "POST":
        if request.POST.get("delete_items") is not None:
            # Fetch list of items to delete, by ID
            items_to_delete = request.POST.getlist("delete_items")
            # Delete those items all in one go
            Note.objects.filter(pk__in=items_to_delete).delete()
            return redirect("index")

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

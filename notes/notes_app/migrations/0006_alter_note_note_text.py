# Generated by Django 3.2.7 on 2021-09-22 19:25

import ckeditor.fields
import django.core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0005_alter_note_note_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note_text',
            field=ckeditor.fields.RichTextField(validators=[django.core.validators.MaxLengthValidator(200)]),
        ),
    ]
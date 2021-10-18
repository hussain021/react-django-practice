# Generated by Django 3.2.8 on 2021-10-18 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.TextField(unique=True, verbose_name='game')),
                ('description', models.TextField(verbose_name='game_description')),
                ('all_reviews', models.CharField(max_length=20, verbose_name='all_reviews')),
                ('all_reviews_count', models.CharField(max_length=10, verbose_name='all_review_count')),
                ('release_date', models.CharField(max_length=40, verbose_name='release_date')),
                ('developer', models.CharField(max_length=40, verbose_name='developer')),
                ('publisher', models.CharField(max_length=40, verbose_name='publisher')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='review_id')),
                ('is_recommended', models.BooleanField(default=True, verbose_name='is_recommended')),
                ('posted_date', models.DateField(verbose_name='posted_date')),
                ('text', models.TextField(verbose_name='text')),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.game', verbose_name='game_id')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='image_id')),
                ('image_path', models.CharField(max_length=100, verbose_name='image_path')),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.game', verbose_name='game_id')),
            ],
        ),
    ]

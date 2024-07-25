# Generated by Django 5.0.6 on 2024-07-25 10:27

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie_back", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("country", models.CharField(blank=True, max_length=50, null=True)),
                ("director", models.CharField(blank=True, max_length=50, null=True)),
                ("duration", models.IntegerField(blank=True, null=True)),
                ("year", models.CharField(blank=True, max_length=50, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("nameRU", models.CharField(blank=True, max_length=100, null=True)),
                ("nameEN", models.CharField(blank=True, max_length=100, null=True)),
                ("image", models.CharField(blank=True, max_length=300, null=True)),
                (
                    "trailerLink",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                ("thumbnail", models.CharField(blank=True, max_length=300, null=True)),
                ("owner", models.UUIDField(blank=True, null=True)),
                ("movieId", models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]

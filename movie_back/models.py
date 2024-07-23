from django.db import models

import uuid


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # movie_id = models.UUIDField(blank=True, null=True)
    nameRu = models.CharField(max_length=100, blank=True, null=True)
    nameEn = models.CharField(max_length=100, blank=True, null=True)
    image = models.CharField(max_length=300)
    country = models.CharField(max_length=50, blank=True, null=True)
    director = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    trailerLink = models.CharField(max_length=300, blank=True, null=True)
    thumbnail = models.CharField(max_length=300, blank=True, null=True)


class User(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=3000)


class Token(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    token = models.CharField(max_length=250, default="token")
    user_id = models.UUIDField(default=uuid.uuid4)

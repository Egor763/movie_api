from django.db import models

import uuid


class Movie(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.CharField(max_length=50, blank=True, null=True)
    director = models.CharField(max_length=50, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    year = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    nameRU = models.CharField(max_length=100, blank=True, null=True)
    nameEN = models.CharField(max_length=100, blank=True, null=True)
    image = models.CharField(max_length=300, blank=True, null=True)
    trailerLink = models.CharField(max_length=300, blank=True, null=True)
    thumbnail = models.CharField(max_length=300, blank=True, null=True)
    owner = models.UUIDField(blank=True, null=True)
    movieId = models.IntegerField(blank=True, null=True)


class User(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=3000, blank=True, null=True)


class Token(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    token = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.UUIDField(blank=True, null=True)

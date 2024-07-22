from django.db import models

import uuid


class Movie(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=300)


class User(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=3000)


class Token(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    token = models.CharField(max_length=250, default="token")
    user_id = models.UUIDField(default=uuid.uuid4)

from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=32)
    reg_date = models.DateTimeField('registration date')
    image = models.ImageField(upload_to='img', null=True, blank=True)
    is_logged = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Room(models.Model):
    color = models.CharField(max_length=20)
    reg_date = models.DateTimeField('registration date')
    redact_date = models.DateTimeField('last modified date')
    description = models.TextField()

    def __str__(self):
        return self.color


class Reserv(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # time = models.DateTimeField('reservation time')

    def __str__(self):
        return self.tag

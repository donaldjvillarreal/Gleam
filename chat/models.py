# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime


class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)
    therapist = models.ForeignKey(User)
    patient = models.ForeignKey(User)


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages')
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

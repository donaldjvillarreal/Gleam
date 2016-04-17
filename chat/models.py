# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime


class ChatMessage(models.Model):
    message = models.CharField(max_length=300)
    room = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(default=datetime.now())

    class Meta(object):
        unique_together = (('message', 'user', 'room', 'timestamp'),)

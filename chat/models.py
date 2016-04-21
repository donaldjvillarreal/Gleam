# coding=utf-8
"""
https://github.com/jacobian/channels-example/blob/master/chat/models.py
"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Room(models.Model):
    label = models.SlugField(unique=True)
    therapist = models.ForeignKey(User, related_name='therapist_user')
    patient = models.ForeignKey(User)

    def __unicode__(self):
        return self.label


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages')
    handle = models.ForeignKey(User)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __unicode__(self):
        return '[{timestamp}] {handle}: {message}'.format(**self.as_dict())

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%m/%d/%y %H:%M:%S')

    def as_dict(self):
        return {'handle': self.handle.username, 'message': self.message, 'timestamp': self.formatted_timestamp}

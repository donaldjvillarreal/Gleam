# coding=utf-8
"""
https://github.com/jacobian/channels-example/blob/master/chat/models.py
"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

import json
from channels import Group


class Room(models.Model):
    label = models.SlugField(unique=True)
    therapist = models.ForeignKey(User, related_name='therapist_user')
    patient = models.ForeignKey(User)

    def __unicode__(self):
        return self.label

    @property
    def websocket_group(self):
        """
        Returns the Channels Group that sockets should subscribe to to get sent
        messages as they are generated.
        """
        return Group("room-%s" % self.id)

    def send_message(self, message, user, timestamp, urgency=''):
        """
        Called to send a message to the room on behalf of a user.
        """
        # Send out the message to everyone in the room
        self.websocket_group.send({
            "text": json.dumps({
                "room": str(self.id),
                "message": message,
                "username": user.username,
                'timestamp': timestamp,
                'urgency': urgency
            }),
        })

    def patient_as_dict(self):
        return {'firstName': self.patient.first_name,
                'lastName': self.patient.last_name,
                'fullName': self.patient.first_name + ' ' + self.patient.last_name,
                'username': self.patient.username}

    def therapist_as_dict(self):
        return {'firstName': self.therapist.first_name,
                'lastName': self.therapist.last_name,
                'fullName': self.therapist.first_name + ' ' + self.patient.last_name,
                'username': self.therapist.username}


class Message(models.Model):
    URGENCY = (('minor', 'Minor'),
               ('moderate', 'Moderate'),
               ('important', 'Important'),
               ('emergency', 'Emergency'))
    room = models.ForeignKey(Room, related_name='messages')
    handle = models.ForeignKey(User)
    message = models.TextField()
    read = models.BooleanField(default=False)
    urgency = models.CharField(max_length=50, blank=True, null=True, choices=URGENCY)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __unicode__(self):
        return '[{timestamp}] {handle}: {message}'.format(**self.as_dict())

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%m/%d/%y %H:%M:%S')

    def as_dict(self):
        return {'handle': self.handle.username,
                'message': self.message,
                'timestamp': self.formatted_timestamp,
                'read': self.read,
                'urgency': self.urgency}

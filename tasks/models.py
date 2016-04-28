# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from authenticate.models import UserProfile
from authenticate.models import Therapist


class MainTask(models.Model):
    therapist = models.ForeignKey(Therapist)
    patient = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=30, blank=False, null=False)
    task = models.TextField()
    deadline = models.DateTimeField()
    completed = models.BooleanField(default=False)
    completed_on = models.DateTimeField(null=True, blank=True)
    # created = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(blank=False, null=False)

    def __unicode__(self):
        return self.patient.user.username + ' ' + self.title + ' completed: ' + str(self.completed)

    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed,
            'completed_on': str(self.completed_on),
            'created': str(self.created)
        }


class SubTask(models.Model):
    order = models.PositiveSmallIntegerField()
    main_task = models.ForeignKey(MainTask)
    task = models.TextField()
    completed = models.BooleanField(default=False)
    completed_on = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.task

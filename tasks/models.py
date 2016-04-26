from __future__ import unicode_literals

from django.db import models
from authenticate.models import UserProfile
from authenticate.models import Therapist


# Create your models here.
class TaskGroup(models.Model):
    therapist = models.ForeignKey(Therapist)
    patient = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=30, blank=False, null=False)
    # created = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(blank=False, null=False)

    def __unicode__(self):
        return self.patient.user.username + self.title


class IndividualTask(models.Model):
    order = models.PositiveSmallIntegerField(blank=False, null=False)
    taskGroup = models.ForeignKey(TaskGroup)
    task = models.TextField(blank=False, null=False)
    completed = models.BooleanField(default=0, blank=False, null=False)

    def __unicode__(self):
        return self.task
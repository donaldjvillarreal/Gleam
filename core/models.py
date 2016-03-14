# coding=utf-8
from django.db import models
from django.contrib.auth.models import User


class ProgressIssue(models.Model):
    """
    Model to gather stats on issues that hinder a user's progress in their regime
    """
    user = models.ForeignKey(User)

    work = models.BooleanField(default=False, blank=True)
    access_to_computer = models.BooleanField(default=False, blank=True)
    time_commitment = models.BooleanField(default=False, blank=True)
    motivation = models.BooleanField(default=False, blank=True)
    forgetfulness = models.BooleanField(default=False, blank=True)
    tired = models.BooleanField(default=False, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        unique_together = ('user', 'created_on',)

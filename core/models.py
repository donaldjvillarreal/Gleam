# coding=utf-8
from django.db import models
from django.contrib.auth.models import User


class ProgressIssue(models.Model):
    """
    Model to gather stats on issues that hinder a user's progress in their regime
    """
    user = models.ForeignKey(User)

    work = models.BooleanField(default=False)
    access_to_computer = models.BooleanField(default=False)
    time_commitment = models.BooleanField(default=False)
    motivation = models.BooleanField(default=False)
    forgetfulness = models.BooleanField(default=False)
    tired = models.BooleanField(default=False)


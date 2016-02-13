# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):
    name = models.CharField(max_length=300)

    def __unicode__(self):
        return self.name


class Question(models.Model):
    survey = models.ForeignKey(Survey)
    text = models.CharField(max_length=500)
    label = models.CharField(max_length=300, blank=True, null=True)

    def __unicode__(self):
        return self.text


class Answer(models.Model):
    value = models.PositiveSmallIntegerField(default=0)
    response = models.CharField(max_length=300)

    question = models.ForeignKey(Question)


class SurveySet(models.Model):
    user = models.ForeignKey(User)
    answers = models.ManyToManyField(Answer)

    completed_on = models.DateTimeField(blank=True, null=True)

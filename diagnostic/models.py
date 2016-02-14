# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):
    """
    Model for basic survey info
    """
    name = models.CharField(max_length=300)
    short_name = models.CharField(max_length=60, null=True)

    def __unicode__(self):
        return self.name


class Question(models.Model):
    """
    Model for a question for a survey
    """
    survey = models.ForeignKey(Survey)
    text = models.CharField(max_length=500)
    label = models.CharField(max_length=300, blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):
        return "%s / %s" % (self.survey.short_name, self.text)

    class Meta:
        unique_together = (("survey", "text"),)


class Answer(models.Model):
    """
    Fixed answers for surveys
    """
    value = models.PositiveSmallIntegerField(default=0)
    response = models.CharField(max_length=300)

    question = models.ForeignKey(Question)

    def __unicode__(self):
        return "%s / %s / %s / %s" % (self.question.survey.short_name, self.question.text, self.response, self.value)

    class Meta:
        unique_together = (("response", "question"),)


class SurveySet(models.Model):
    """
    Model to store user responses to surveys
    """
    user = models.ForeignKey(User)
    survey = models.ForeignKey(Survey)
    answer = models.ForeignKey(Answer, null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    completed_on = models.DateTimeField(blank=True, null=True)

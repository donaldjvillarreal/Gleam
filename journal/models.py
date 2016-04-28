# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime

from authenticate.models import Therapist


class Entry(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=60, null=False, blank=False)
    # created = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(null=False, blank=False)
    entry = models.TextField()
    sentiment_type = models.CharField(max_length=25, null=False, blank=False)
    sentiment_score = models.DecimalField(max_digits=10, decimal_places=6, null=False, blank=False)

    def __unicode__(self):
        return self.user.username + ' ' + self.title

    class Meta(object):
        verbose_name_plural = 'entries'


class Keywords(models.Model):
    entry = models.ForeignKey(Entry)
    text = models.CharField(max_length=50, null=False, blank=False)
    relevance = models.DecimalField(max_digits=10, decimal_places=6, null=False, blank=False)
    sentiment_type = models.CharField(max_length=25, null=False, blank=False)
    sentiment_score = models.DecimalField(max_digits=10, decimal_places=6, null=False, blank=False)

    def __unicode__(self):
        return self.text

    class Meta(object):
        verbose_name_plural = 'keywords'


class Entities(models.Model):
    entry = models.ForeignKey(Entry)
    entity_type = models.CharField(max_length=50, null=False, blank=False)
    relevance = models.DecimalField(max_digits=10, decimal_places=6, null=False, blank=False)
    count = models.IntegerField(default=0)
    text = models.CharField(max_length=50, null=False, blank=False)
    sentiment_type = models.CharField(max_length=25, null=False, blank=False)
    sentiment_score = models.DecimalField(max_digits=10, decimal_places=6, null=False, blank=False)

    def __unicode__(self):
        return self.text

    class Meta(object):
        verbose_name_plural = 'entities'


class Note(models.Model):
    note = models.TextField()
    title = models.CharField(max_length=60, null=False, blank=False)
    therapist = models.ForeignKey(Therapist)

    created_on = models.DateTimeField(default=datetime.now())

    def __unicode__(self):
        return self.therapist.user_profile.user.username + ' ' + self.title[:30]

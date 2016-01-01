# coding=utf-8
"""
Models for different tracks
There's a many-to-many relationship between tracks and track items. Consider the case where a track can have a item
from a different track. This makes efficient use of pre-existing track items.
"""
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class TrackItem(models.Model):
    """
    Node which makes up a track
    """
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Track Item'


class Track(models.Model):
    """
    Holds the track item nodes and also the title and overall description of the track
    """
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    items = models.ManyToManyField(TrackItem, through='TrackOrder')

    def __unicode__(self):
        return self.title


class TrackOrder(models.Model):
    """
    Allows same track items to be used in different tracks with different ordering.
    """
    track = models.ForeignKey(Track)
    track_item = models.ForeignKey(TrackItem)
    rank = models.PositiveIntegerField()

    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.user.username + ', ' + self.track.title + ', ' + str(self.rank)

    class Meta:
        verbose_name = 'Track Order'


class TrackInformation(models.Model):
    """
    This model specifies who a track is meant for
    """
    created = models.DateTimeField(auto_now_add=True)

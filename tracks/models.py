# coding=utf-8
"""
Models for different tracks
There's a many-to-many relationship between tracks and track items. Consider the case where a track can have a item
from a different track. This makes efficient use of pre-existing track items.
"""
from __future__ import unicode_literals

from django.db import models


class TrackItem(models.Model):
    """
    Node which makes up a track
    """
    description = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField()


class Track(models.Model):
    """
    Holds the track item nodes and also the title and overall description of the track
    """
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=500)

    items = models.ManyToManyField(TrackItem)

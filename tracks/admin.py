# coding=utf-8
from django.contrib import admin

from tracks import models

admin.site.register(models.Track)
admin.site.register(models.TrackItem)
admin.site.register(models.TrackOrder)
# admin.site.register(models.TrackInformation)
# coding=utf-8
from django.contrib import admin
from journal import models


admin.site.register(models.journalEntry)
admin.site.register(models.keywords)
admin.site.register(models.entities)
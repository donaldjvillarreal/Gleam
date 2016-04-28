# coding=utf-8
from django.contrib import admin
from journal import models

admin.site.register(models.Entry)
admin.site.register(models.Note)
admin.site.register(models.Keywords)
admin.site.register(models.Entities)

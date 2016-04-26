# coding=utf-8
from django.contrib import admin
from tasks import models

# Register your models here.
admin.site.register(models.MainTask)
admin.site.register(models.SubTask)

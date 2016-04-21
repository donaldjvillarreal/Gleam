# coding=utf-8
from django.contrib import admin
from chat import models

admin.site.register(models.Message)

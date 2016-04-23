# coding=utf-8
from django.contrib import admin
from authenticate import models

# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.Client)
admin.site.register(models.Therapist)

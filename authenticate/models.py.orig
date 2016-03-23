# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    points = models.IntegerField(default=0)

    # The additional attributes we wish to include.
    GENDER = (('M','Male'),
              ('F','Female'),
              ('U','Prefer Not to Answer'))
    
    gender = models.CharField(max_length=1,
                              choices=GENDER,
                              default='U')
    picture = models.ImageField(upload_to='static/profile_images', null=True, blank=True)

    dob = models.DateField(null=False, blank=False)

    timezone = models.IntegerField(default=0, null=False, blank=False)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
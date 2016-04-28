# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.conf import settings


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    points = models.IntegerField(default=0)

    GENDER = (('M', 'Male'),
              ('F', 'Female'),
              ('U', 'Prefer Not to Answer'))

    gender = models.CharField(max_length=1,
                              choices=GENDER,
                              default='U')
    # TODO: Change to STATIC_URL
    picture = models.ImageField(upload_to=settings.PROFILE_IMAGES, null=True, blank=True,
                                default=static('images/user.png'))

    dob = models.DateField(null=False, blank=False)

    timezone = models.IntegerField(default=0)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: "
                                                                   "'+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], blank=True, null=True, max_length=10)

    subscribed = models.BooleanField(blank=False, null=False, default=False)

    # Good way to quickly check type of user
    is_therapist = models.BooleanField(default=False)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Therapist(models.Model):
    user_profile = models.OneToOneField(UserProfile)
    practice = models.CharField(max_length=60, null=False, blank=False)
    address = models.CharField(max_length=60, null=False, blank=False)
    city = models.CharField(max_length=60, null=False, blank=False)
    state = models.CharField(max_length=2, null=False, blank=False)
    zip = models.CharField(max_length=5, null=False, blank=False)

    def __unicode__(self):
        return self.user_profile.user.username

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.user_profile.is_therapist = True
        super(Therapist, self).save()


class Client(models.Model):
    therapist = models.ForeignKey(Therapist)
    user_profile = models.OneToOneField(UserProfile)

    def __unicode__(self):
        return self.therapist.user_profile.user.username + "->" + self.user_profile.user.username

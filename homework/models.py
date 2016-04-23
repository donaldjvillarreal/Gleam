from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class homework(models.Model)
    owner = models.ForeignKey(Therapist)
    user = models.ForeignKey(User)
    title = models.CharField(max_length=30, blank=False, null=False)
    created = models.DateTimeField(auto_created=True, blank=False, null=False)

    def __unicode__(self):
        return self.user.username + self.title


class hwQuestions(models.Model)
    hw = models.ForeignKey(homework)
    question = models.TextField(blank=False, null=False)

    def __unicode__(self):
        return self.question


class hwAnswers(models.Model)
    question = models.ForeignKey(hwQuestions)
    answer = models.TextField(blank=False, null=False)

    def __unicode__(self):
        return self.answer

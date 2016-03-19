# coding=utf-8

from core import models
from django import forms


class ProgressIssueForm(forms.ModelForm):
    class Meta(object):
        model = models.ProgressIssue
        exclude = ('user',)

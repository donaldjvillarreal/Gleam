# coding=utf-8
from django import forms
from journal import models


class entryForm(forms.ModelForm):
    class Meta(object):
        model = models.journalEntry
        fields = ('entry',)

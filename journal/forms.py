# coding=utf-8
from django import forms
from journal import models


class entryForm(forms.ModelForm):
    created = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'])

    class Meta(object):
        model = models.journalEntry
        fields = ('entry', 'title', 'created', )
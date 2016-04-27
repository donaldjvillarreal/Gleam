# coding=utf-8
from django import forms
from journal import models


class EntryForm(forms.ModelForm):
    created = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'])

    class Meta(object):
        model = models.Entry
        fields = ('entry', 'title', 'created', )
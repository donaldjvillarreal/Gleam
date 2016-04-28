# coding=utf-8
from django import forms
from journal import models


class EntryForm(forms.ModelForm):
    created = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'])

    class Meta(object):
        model = models.Entry
        fields = ('entry', 'title', 'created',)


class NoteForm(forms.ModelForm):
    created_on = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'])

    class Meta(object):
        model = models.Note
        fields = ('note', 'title', 'created_on',)

# coding=utf-8
from django import forms
from tasks import models


class MainTaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(input_formats=['%d-%m-%Y %H:%M'])

    class Meta(object):
        model = models.MainTask
        fields = ('title', 'task', 'deadline')

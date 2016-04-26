# coding=utf-8
from django import forms
from tasks import models


class CreateTaskGroup(forms.ModelForm):
    created = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'])

    class Meta(object):
        model = models.TaskGroup
        fields = ('title', 'created')

class CreateTasks(forms.ModelForm):
    class Meta(object):
        model = models.IndividualTask
        fields = ('order', 'task', )

class TaskList(forms.ModelForm):
    class Meta(object):
        model = models.IndividualTask
        fields = ('completed', )
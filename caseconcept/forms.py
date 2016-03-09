# coding=utf-8
from django import forms
from django.contrib.auth.models import User
from caseconcept import models


class ProblemAspectForm(forms.ModelForm):
    class Meta(object):
        model = models.ProblemAspect
        exclude = ('user',)


class ProblemAspectSituationForm(forms.ModelForm):
    class Meta(object):
        model = models.ProblemAspectSituation
        exclude = ('problem',)


class ProblemGoalForm(forms.ModelForm):
    class Meta(object):
        model = models.ProblemGoal
        exclude = ('user', 'problem',)


class ProblemGoalRankingForm(forms.ModelForm):
    class Meta(object):
        model = models.ProblemGoalRanking
        exclude = ('user', )


class PlannerForm(forms.ModelForm):
    class Meta(object):
        model = models.PracticeCalendar
        fields = ('weekday_time',)

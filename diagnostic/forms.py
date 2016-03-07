# coding=utf-8

from django import forms
from diagnostic import models


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

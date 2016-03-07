# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from diagnostic.case_options import SEVERITY_CHOICES, FREQUENCY_CHOICES, goal_frequencies


class Survey(models.Model):
    """
    Model for basic survey info
    """
    name = models.CharField(max_length=300)
    short_name = models.CharField(max_length=60, null=True)

    def __unicode__(self):
        return self.name


class Question(models.Model):
    """
    Model for a question for a survey
    """
    survey = models.ForeignKey(Survey)
    text = models.CharField(max_length=500)
    label = models.CharField(max_length=300, blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):
        return "%s / %s" % (self.survey.short_name, self.text)

    class Meta(object):
        unique_together = (("survey", "text"),)


class Answer(models.Model):
    """
    Fixed answers for surveys
    """
    value = models.PositiveSmallIntegerField(default=0)
    response = models.CharField(max_length=300)

    question = models.ForeignKey(Question)

    def __unicode__(self):
        return "%s / %s / %s / %s" % (self.question.survey.short_name, self.question.text, self.response, self.value)

    class Meta(object):
        unique_together = (("response", "question"),)


class SurveySet(models.Model):
    """
    Model to store user responses to surveys
    """
    user = models.ForeignKey(User)
    survey = models.ForeignKey(Survey)
    answer = models.ManyToManyField(Answer)

    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    completed_on = models.DateTimeField(blank=True, null=True)


# Case conceptualization
class ProblemAspect(models.Model):
    """
    Negative aspects affected by depression
    """
    user = models.ForeignKey(User)  # Lets us set some pre-defined aspects
    text = models.CharField(max_length=50)
    frequency = models.SmallIntegerField(choices=FREQUENCY_CHOICES)
    severity = models.SmallIntegerField(choices=SEVERITY_CHOICES)
    improve = models.BooleanField(blank=True, default=False)

    def __unicode__(self):
        return self.text[:40]

    def frequency_verbose(self):
        return FREQUENCY_CHOICES[self.frequency][1]

    def severity_verbose(self):
        return SEVERITY_CHOICES[self.severity][1]


class ProblemAspectSituation(models.Model):
    """
    This model is for the explanation of how the problem aspect has affected the user's life
    """
    DISTRESS_LEVEL_CHOICES = ((i, i) for i in range(0, 11))
    problem = models.ForeignKey(ProblemAspect)
    situation = models.CharField(max_length=300)
    thought = models.CharField(max_length=300)
    feeling = models.CharField(max_length=300)
    reaction = models.CharField(max_length=300)
    distress_level = models.SmallIntegerField(choices=DISTRESS_LEVEL_CHOICES)

    def __unicode__(self):
        return self.problem.__unicode__()


class ProblemGoal(models.Model):
    user = models.ForeignKey(User, null=True)
    problem = models.ForeignKey(ProblemAspect)

    action = models.CharField(max_length=300, blank=True, null=True)
    frequency = models.SmallIntegerField()

    def frequency_verbose(self):
        return goal_frequencies[self.frequency - 1][0]

    def __unicode__(self):
        return self.action[:40]


class ProblemGoalRanking(models.Model):
    user = models.ForeignKey(User)

    first = models.ForeignKey(ProblemGoal, related_name='problemgoalranking_first')
    second = models.ForeignKey(ProblemGoal, related_name='problemgoalranking_second', null=True, blank=True)
    third = models.ForeignKey(ProblemGoal, related_name='problemgoalranking_third', null=True, blank=True)

    current_goal = models.ForeignKey(ProblemGoal, related_name='problemgoalranking_current', null=True, blank=True)

    class Meta(object):
        unique_together = (('user', 'first', 'second', 'third'),)

    def __unicode__(self):
        if self.current_goal is not None:
            return '%s\'s current goal: %s' % (self.user.username, self.current_goal.__unicode__())
        else:
            return '%s\'s current goal: none' % self.user.username

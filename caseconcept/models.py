# coding=utf-8
from django.db import models
from django.contrib.auth.models import User


from caseconcept.case_options import FREQUENCY_CHOICES, SEVERITY_CHOICES, goal_frequencies


class ProblemAspect(models.Model):
    """
    Negative aspects affected by depression
    """
    user = models.ForeignKey(User)  # Lets us set some pre-defined aspects
    text = models.CharField(max_length=50, unique=True)
    frequency = models.SmallIntegerField(choices=FREQUENCY_CHOICES)
    severity = models.SmallIntegerField(choices=SEVERITY_CHOICES)
    improve = models.BooleanField(blank=True, default=False)

    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text

    def frequency_verbose(self):
        return FREQUENCY_CHOICES[self.frequency][1]

    def severity_verbose(self):
        return SEVERITY_CHOICES[self.severity][1]

    class Meta(object):
        get_latest_by = 'created'


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

    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.problem.__unicode__()

    class Meta(object):
        get_latest_by = 'created'


class ProblemGoal(models.Model):
    user = models.ForeignKey(User, null=True)
    problem = models.ForeignKey(ProblemAspect)

    action = models.CharField(max_length=300, blank=True, null=True)
    frequency = models.SmallIntegerField()

    created = models.DateTimeField(auto_now_add=True)
    stale = models.BooleanField(default=True)

    def frequency_verbose(self):
        return goal_frequencies[self.frequency - 1][0]

    def __unicode__(self):
        return self.action[:40]

    class Meta(object):
        get_latest_by = 'created'
        unique_together = (('user', 'problem', 'frequency'),)


class ProblemGoalRanking(models.Model):
    user = models.ForeignKey(User)

    first = models.ForeignKey(ProblemGoal, related_name='problemgoalranking_first')
    second = models.ForeignKey(ProblemGoal, related_name='problemgoalranking_second', null=True, blank=True)
    third = models.ForeignKey(ProblemGoal, related_name='problemgoalranking_third', null=True, blank=True)

    current_goal = models.ForeignKey(ProblemGoal, related_name='problemgoalranking_current', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        unique_together = (('user', 'first', 'second', 'third'),)
        get_latest_by = 'created'

    def __unicode__(self):
        if self.current_goal is not None:
            return '%s\'s current goal: %s' % (self.user.username, self.current_goal.__unicode__())
        else:
            return '%s\'s current goal: none' % self.user.username


class PracticeCalendar(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.ForeignKey(User)
    goal = models.ForeignKey(ProblemGoal)

    weekday_time = models.CharField(max_length=5)

    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s, %s' % (self.user.username, self.weekday_time)

    class Meta(object):
        unique_together = (('goal', 'weekday_time'),)
        get_latest_by = 'created'

# coding=utf-8
from django.contrib import admin
from diagnostic import models

# Register your models here.
admin.site.register(models.Survey)
admin.site.register(models.Question)
admin.site.register(models.Answer)
admin.site.register(models.SurveySet)
admin.site.register(models.ProblemAspect)
admin.site.register(models.ProblemAspectSituation)
admin.site.register(models.ProblemGoal)
admin.site.register(models.ProblemGoalRanking)

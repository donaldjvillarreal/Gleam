# coding=utf-8
from django.contrib import admin
from caseconcept import models


admin.site.register(models.PracticeCal)
admin.site.register(models.ProblemAspect)
admin.site.register(models.ProblemAspectSituation)
admin.site.register(models.ProblemGoal)
admin.site.register(models.ProblemGoalRanking)
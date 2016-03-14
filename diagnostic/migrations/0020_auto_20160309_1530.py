# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic', '0019_auto_20160307_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problemaspect',
            name='user',
        ),
        migrations.RemoveField(
            model_name='problemaspectsituation',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='problemgoal',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='problemgoal',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='problemgoalranking',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='problemgoalranking',
            name='current_goal',
        ),
        migrations.RemoveField(
            model_name='problemgoalranking',
            name='first',
        ),
        migrations.RemoveField(
            model_name='problemgoalranking',
            name='second',
        ),
        migrations.RemoveField(
            model_name='problemgoalranking',
            name='third',
        ),
        migrations.RemoveField(
            model_name='problemgoalranking',
            name='user',
        ),
        migrations.RemoveField(
            model_name='surveyset',
            name='answer',
        ),
        migrations.AddField(
            model_name='surveyset',
            name='answer',
            field=models.ForeignKey(blank=True, to='diagnostic.Answer', null=True),
        ),
        migrations.DeleteModel(
            name='ProblemAspect',
        ),
        migrations.DeleteModel(
            name='ProblemAspectSituation',
        ),
        migrations.DeleteModel(
            name='ProblemGoal',
        ),
        migrations.DeleteModel(
            name='ProblemGoalRanking',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic', '0016_problemgoalranking_current_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemgoalranking',
            name='second',
            field=models.ForeignKey(related_name='problemgoalranking_second', blank=True, to='diagnostic.ProblemGoal', null=True),
        ),
        migrations.AlterField(
            model_name='problemgoalranking',
            name='third',
            field=models.ForeignKey(related_name='problemgoalranking_third', blank=True, to='diagnostic.ProblemGoal', null=True),
        ),
    ]

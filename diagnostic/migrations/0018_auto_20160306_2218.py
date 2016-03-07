# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic', '0017_auto_20160306_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemgoalranking',
            name='current_goal',
            field=models.ForeignKey(related_name='problemgoalranking_current', blank=True, to='diagnostic.ProblemGoal', null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic', '0015_auto_20160306_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemgoalranking',
            name='current_goal',
            field=models.ForeignKey(blank=True, to='diagnostic.ProblemGoal', null=True),
        ),
    ]

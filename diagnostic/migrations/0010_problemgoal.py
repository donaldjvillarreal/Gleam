# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic', '0009_problemaspectsituation_reaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemGoal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.CharField(max_length=300, null=True, blank=True)),
                ('frequency', models.SmallIntegerField()),
                ('problem', models.ForeignKey(to='diagnostic.ProblemAspect')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic', '0003_auto_20160305_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemaspect',
            name='improve',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='problemaspectsituation',
            name='problem',
            field=models.ForeignKey(to='diagnostic.ProblemAspect', null=True),
        ),
        migrations.AlterField(
            model_name='problemaspectsituation',
            name='distress_level',
            field=models.SmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
        ),
    ]

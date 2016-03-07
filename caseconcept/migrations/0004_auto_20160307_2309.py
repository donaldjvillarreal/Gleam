# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caseconcept', '0003_auto_20160307_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practicecal',
            name='TimePlan',
        ),
        migrations.RemoveField(
            model_name='practicecal',
            name='WeekdayPlan',
        ),
        migrations.AddField(
            model_name='practicecal',
            name='WeekdayTime',
            field=models.CharField(default=10000, max_length=5),
            preserve_default=False,
        ),
    ]

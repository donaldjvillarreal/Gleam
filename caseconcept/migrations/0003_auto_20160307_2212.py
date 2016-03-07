# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caseconcept', '0002_auto_20160307_1805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='practicecal',
            old_name='WeekdayTime',
            new_name='TimePlan',
        ),
        migrations.AddField(
            model_name='practicecal',
            name='WeekdayPlan',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caseconcept', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='practicecal',
            old_name='wdaypractice',
            new_name='WeekdayTime',
        ),
        migrations.RemoveField(
            model_name='practicecal',
            name='timepractice',
        ),
    ]

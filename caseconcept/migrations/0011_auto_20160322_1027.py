# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('caseconcept', '0010_auto_20160322_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicecalendar',
            name='goal',
            field=models.OneToOneField(to='caseconcept.ProblemGoal'),
        ),
    ]

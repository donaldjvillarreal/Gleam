# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caseconcept', '0005_auto_20160308_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicecal',
            name='WeekdayTime',
            field=models.CharField(max_length=5),
        ),
    ]

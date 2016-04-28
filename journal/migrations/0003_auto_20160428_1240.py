# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):
    dependencies = [
        ('journal', '0002_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 28, 12, 39, 56, 377000)),
        ),
    ]

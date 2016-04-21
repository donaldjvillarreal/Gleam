# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):
    dependencies = [
        ('chat', '0003_auto_20160416_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='patient',
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 16, 22, 35, 56)),
        ),
    ]

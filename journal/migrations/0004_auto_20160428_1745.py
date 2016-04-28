# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):
    dependencies = [
        ('journal', '0003_auto_20160428_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 28, 17, 45, 49, 532000)),
        ),
        migrations.AlterField(
            model_name='note',
            name='therapist',
            field=models.ForeignKey(to='authenticate.Therapist'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('tasks', '0005_auto_20160426_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintask',
            name='completed_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 27, 1, 32, 14, 380000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subtask',
            name='completed_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 27, 1, 32, 17, 855000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

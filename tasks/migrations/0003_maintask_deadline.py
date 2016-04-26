# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('tasks', '0002_auto_20160426_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintask',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 26, 18, 40, 57, 790000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

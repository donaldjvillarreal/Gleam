# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='progressissue',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 7, 20, 2, 49, 899000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='progressissue',
            unique_together=set([('user', 'created_on')]),
        ),
    ]

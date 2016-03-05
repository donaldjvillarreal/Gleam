# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic', '0005_auto_20160305_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemaspect',
            name='default',
            field=models.BooleanField(default=False),
        ),
    ]

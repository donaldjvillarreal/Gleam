# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic', '0006_problemaspect_default'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problemaspect',
            name='default',
        ),
    ]

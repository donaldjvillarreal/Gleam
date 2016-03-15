# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('caseconcept', '0002_auto_20160314_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemgoal',
            name='stale',
            field=models.BooleanField(default=False),
        ),
    ]

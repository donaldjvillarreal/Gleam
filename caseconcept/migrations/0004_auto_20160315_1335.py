# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('caseconcept', '0003_problemgoal_stale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemgoal',
            name='stale',
            field=models.BooleanField(default=True),
        ),
    ]

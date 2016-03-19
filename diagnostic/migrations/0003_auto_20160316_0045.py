# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('diagnostic', '0002_auto_20160316_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyset',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='sessions.Session',
                                    null=True),
        ),
    ]

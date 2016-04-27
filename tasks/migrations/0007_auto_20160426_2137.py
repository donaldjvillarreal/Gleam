# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('tasks', '0006_auto_20160426_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintask',
            name='completed_on',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='completed_on',
            field=models.DateTimeField(null=True),
        ),
    ]

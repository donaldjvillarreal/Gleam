# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('tasks', '0003_maintask_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintask',
            name='deadline',
            field=models.DateTimeField(null=True),
        ),
    ]

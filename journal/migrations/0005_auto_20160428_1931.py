# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('journal', '0004_auto_20160428_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created_on',
            field=models.DateTimeField(),
        ),
    ]

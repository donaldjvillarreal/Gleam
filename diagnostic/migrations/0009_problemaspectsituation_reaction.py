# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic', '0008_auto_20160305_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemaspectsituation',
            name='reaction',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]

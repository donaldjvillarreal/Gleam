# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('caseconcept', '0007_auto_20160321_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemaspectsituation',
            name='summary',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('caseconcept', '0006_auto_20160315_1352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problemaspectsituation',
            name='feeling',
        ),
        migrations.RemoveField(
            model_name='problemaspectsituation',
            name='thought',
        ),
        migrations.AddField(
            model_name='problemaspectsituation',
            name='thoughts_and_feelings',
            field=models.CharField(default='', max_length=600),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic', '0004_auto_20160305_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemaspectsituation',
            name='problem',
            field=models.ForeignKey(to='diagnostic.ProblemAspect'),
        ),
    ]

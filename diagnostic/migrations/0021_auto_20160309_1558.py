# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic', '0020_auto_20160309_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyset',
            name='answer',
        ),
        migrations.AddField(
            model_name='surveyset',
            name='answer',
            field=models.ManyToManyField(to='diagnostic.Answer'),
        ),
    ]

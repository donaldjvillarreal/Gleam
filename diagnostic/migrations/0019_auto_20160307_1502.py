# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic', '0018_auto_20160306_2218'),
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

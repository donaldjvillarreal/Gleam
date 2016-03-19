# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('sessions', '0001_initial'),
        ('diagnostic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyset',
            name='session',
            field=models.ForeignKey(on_delete=None, blank=True, to='sessions.Session', null=True),
        ),
        migrations.AlterField(
            model_name='surveyset',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]

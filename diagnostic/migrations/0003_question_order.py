# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-14 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic', '0002_auto_20160213_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]

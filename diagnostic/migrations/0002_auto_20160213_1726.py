# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-13 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='label',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]

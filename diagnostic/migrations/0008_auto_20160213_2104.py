# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-14 02:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic', '0007_auto_20160213_2047'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together=set([('response', 'question')]),
        ),
    ]

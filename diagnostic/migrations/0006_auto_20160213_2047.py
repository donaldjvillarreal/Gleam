# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-14 01:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic', '0005_auto_20160213_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyset',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='surveyset',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='surveyset',
            name='survey',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diagnostic.Survey'),
        ),
        migrations.AlterField(
            model_name='surveyset',
            name='answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='diagnostic.Answer'),
        ),
    ]

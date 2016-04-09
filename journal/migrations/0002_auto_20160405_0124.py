# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalentry',
            name='sentimentMixed',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='journalentry',
            name='sentimentScore',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='journalentry',
            name='sentimentType',
            field=models.TextField(default='neutral'),
            preserve_default=False,
        ),
    ]

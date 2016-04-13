# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):
    dependencies = [
        ('authenticate', '0008_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[
                django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$',
                                                      message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
        ),
    ]

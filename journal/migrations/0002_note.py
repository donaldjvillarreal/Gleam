# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.TextField()),
                ('created_on', models.DateTimeField(default=datetime.datetime(2016, 4, 27, 18, 45, 41, 996000))),
                ('therapist', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

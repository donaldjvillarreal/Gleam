# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=300)),
                ('room', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2016, 4, 16, 22, 35, 7, 872000))),
                ('patient', models.ForeignKey(related_name='patient_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='chatmessage',
            unique_together=set([('message', 'user', 'room', 'timestamp')]),
        ),
    ]

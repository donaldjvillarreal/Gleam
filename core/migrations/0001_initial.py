# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgressIssue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work', models.BooleanField(default=False)),
                ('access_to_computer', models.BooleanField(default=False)),
                ('time_commitment', models.BooleanField(default=False)),
                ('motivation', models.BooleanField(default=False)),
                ('forgetfulness', models.BooleanField(default=False)),
                ('tired', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

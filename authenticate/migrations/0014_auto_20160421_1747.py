# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('authenticate', '0013_auto_20160421_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client', models.OneToOneField(to='authenticate.UserProfile')),
                ('therapist', models.ForeignKey(to='authenticate.Therapist')),
            ],
        ),
        migrations.RemoveField(
            model_name='clients',
            name='client',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='therapist',
        ),
        migrations.DeleteModel(
            name='Clients',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diagnostic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemAspect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=50)),
                ('frequency', models.SmallIntegerField(choices=[(0, 'Every day'), (1, 'Once a week'), (2, 'Once a month'), (3, 'Every few months'), (4, 'Other')])),
                ('severity', models.SmallIntegerField(choices=[(0, 'Insignificant'), (1, 'Minor'), (2, 'Serious'), (3, 'Very Serious')])),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemAspectSituations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('situation', models.CharField(max_length=300)),
                ('thought', models.CharField(max_length=300)),
                ('feeling', models.CharField(max_length=300)),
                ('distress_level', models.SmallIntegerField(max_length=300, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('caseconcept', '0007_auto_20160309_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='PracticeCalendar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weekday_time', models.CharField(max_length=5)),
                ('goal', models.ForeignKey(to='caseconcept.ProblemGoal')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='practicecal',
            name='user',
        ),
        migrations.DeleteModel(
            name='PracticeCal',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('caseconcept', '0009_auto_20160321_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarWeekdayTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.SmallIntegerField()),
                ('hour', models.SmallIntegerField()),
                ('minute', models.SmallIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='practicecalendar',
            name='goal',
            field=models.ForeignKey(to='caseconcept.ProblemGoal', unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='practicecalendar',
            unique_together=set([]),
        ),
        migrations.AddField(
            model_name='calendarweekdaytime',
            name='practice_calendar',
            field=models.ForeignKey(to='caseconcept.PracticeCalendar'),
        ),
        migrations.RemoveField(
            model_name='practicecalendar',
            name='user',
        ),
        migrations.RemoveField(
            model_name='practicecalendar',
            name='weekday_time',
        ),
    ]

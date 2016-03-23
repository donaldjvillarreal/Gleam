# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('caseconcept', '0011_auto_20160322_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendarweekdaytime',
            name='practice_calendar',
        ),
        migrations.AddField(
            model_name='practicecalendar',
            name='day',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='practicecalendar',
            name='hour',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='practicecalendar',
            name='minute',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='practicecalendar',
            name='goal',
            field=models.ForeignKey(to='caseconcept.ProblemGoal'),
        ),
        migrations.AlterUniqueTogether(
            name='practicecalendar',
            unique_together=set([('goal', 'day', 'hour', 'minute')]),
        ),
        migrations.DeleteModel(
            name='CalendarWeekdayTime',
        ),
    ]

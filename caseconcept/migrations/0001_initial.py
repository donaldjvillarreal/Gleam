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
            name='PracticeCalendar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weekday_time', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemAspect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=50)),
                ('frequency', models.SmallIntegerField(choices=[(0, b'Every day'), (1, b'Once a week'), (2, b'Once a month'), (3, b'Every few months')])),
                ('severity', models.SmallIntegerField(choices=[(0, b'Very Minor'), (1, b'Minor'), (2, b'Moderate'), (3, b'Serious'), (4, b'Very Serious')])),
                ('improve', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemAspectSituation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('situation', models.CharField(max_length=300)),
                ('thought', models.CharField(max_length=300)),
                ('feeling', models.CharField(max_length=300)),
                ('reaction', models.CharField(max_length=300)),
                ('distress_level', models.SmallIntegerField()),
                ('problem', models.ForeignKey(to='caseconcept.ProblemAspect')),
            ],
        ),
        migrations.CreateModel(
            name='ProblemGoal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.CharField(max_length=300, null=True, blank=True)),
                ('frequency', models.SmallIntegerField()),
                ('problem', models.ForeignKey(to='caseconcept.ProblemAspect')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemGoalRanking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('current_goal', models.ForeignKey(related_name='problemgoalranking_current', blank=True, to='caseconcept.ProblemGoal', null=True)),
                ('first', models.ForeignKey(related_name='problemgoalranking_first', to='caseconcept.ProblemGoal')),
                ('second', models.ForeignKey(related_name='problemgoalranking_second', blank=True, to='caseconcept.ProblemGoal', null=True)),
                ('third', models.ForeignKey(related_name='problemgoalranking_third', blank=True, to='caseconcept.ProblemGoal', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='practicecalendar',
            name='goal',
            field=models.ForeignKey(to='caseconcept.ProblemGoal'),
        ),
        migrations.AddField(
            model_name='practicecalendar',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='problemgoalranking',
            unique_together=set([('user', 'first', 'second', 'third')]),
        ),
        migrations.AlterUniqueTogether(
            name='practicecalendar',
            unique_together=set([('goal', 'weekday_time')]),
        ),
    ]

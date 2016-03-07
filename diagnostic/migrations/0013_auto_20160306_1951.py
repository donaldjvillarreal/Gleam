# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diagnostic', '0012_auto_20160306_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemGoalRanking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='problemgoal',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='problemgoalranking',
            name='first',
            field=models.ForeignKey(related_name='problemgoalranking_first', to='diagnostic.ProblemGoal'),
        ),
        migrations.AddField(
            model_name='problemgoalranking',
            name='second',
            field=models.ForeignKey(related_name='problemgoalranking_second', to='diagnostic.ProblemGoal'),
        ),
        migrations.AddField(
            model_name='problemgoalranking',
            name='third',
            field=models.ForeignKey(related_name='problemgoalranking_third', to='diagnostic.ProblemGoal'),
        ),
        migrations.AddField(
            model_name='problemgoalranking',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='problemgoalranking',
            unique_together=set([('first', 'second', 'third')]),
        ),
    ]

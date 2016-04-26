# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('authenticate', '0002_auto_20160424_1459'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('task', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('created', models.DateTimeField()),
                ('patient', models.ForeignKey(to='authenticate.UserProfile')),
                ('therapist', models.ForeignKey(to='authenticate.Therapist')),
            ],
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveSmallIntegerField()),
                ('task', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('main_task', models.ForeignKey(to='tasks.MainTask')),
            ],
        ),
        migrations.RemoveField(
            model_name='individualtask',
            name='taskGroup',
        ),
        migrations.RemoveField(
            model_name='taskgroup',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='taskgroup',
            name='therapist',
        ),
        migrations.DeleteModel(
            name='IndividualTask',
        ),
        migrations.DeleteModel(
            name='TaskGroup',
        ),
    ]

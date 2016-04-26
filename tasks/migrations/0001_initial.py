# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('authenticate', '0002_auto_20160424_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveSmallIntegerField()),
                ('task', models.TextField()),
                ('completed', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TaskGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('created', models.DateTimeField()),
                ('patient', models.ForeignKey(to='authenticate.UserProfile')),
                ('therapist', models.ForeignKey(to='authenticate.Therapist')),
            ],
        ),
        migrations.AddField(
            model_name='individualtask',
            name='taskGroup',
            field=models.ForeignKey(to='tasks.TaskGroup'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.PositiveSmallIntegerField(default=0)),
                ('response', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=500)),
                ('label', models.CharField(max_length=300, null=True, blank=True)),
                ('order', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAnswerSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.ForeignKey(to='diagnostic.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('short_name', models.CharField(max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SurveySet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('completed_on', models.DateTimeField(null=True, blank=True)),
                ('answers', models.ManyToManyField(to='diagnostic.Answer', through='diagnostic.QuestionAnswerSet')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='sessions.Session', null=True)),
                ('survey', models.ForeignKey(to='diagnostic.Survey')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='questionanswerset',
            name='survey_set',
            field=models.ForeignKey(to='diagnostic.SurveySet'),
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(to='diagnostic.Survey'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='diagnostic.Question'),
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set([('survey', 'text')]),
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together=set([('response', 'question')]),
        ),
    ]

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
            name='Entities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entity_type', models.CharField(max_length=50)),
                ('relevance', models.DecimalField(max_digits=10, decimal_places=6)),
                ('count', models.IntegerField(default=0)),
                ('text', models.CharField(max_length=50)),
                ('sentiment_type', models.CharField(max_length=25)),
                ('sentiment_score', models.DecimalField(max_digits=10, decimal_places=6)),
            ],
            options={
                'verbose_name_plural': 'entities',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('created', models.DateTimeField()),
                ('entry', models.TextField()),
                ('sentiment_type', models.CharField(max_length=25)),
                ('sentiment_score', models.DecimalField(max_digits=10, decimal_places=6)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=50)),
                ('relevance', models.DecimalField(max_digits=10, decimal_places=6)),
                ('sentiment_type', models.CharField(max_length=25)),
                ('sentiment_score', models.DecimalField(max_digits=10, decimal_places=6)),
                ('entry', models.ForeignKey(to='journal.Entry')),
            ],
            options={
                'verbose_name_plural': 'keywords',
            },
        ),
        migrations.AddField(
            model_name='entities',
            name='entry',
            field=models.ForeignKey(to='journal.Entry'),
        ),
    ]

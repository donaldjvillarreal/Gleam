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
            name='entities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entityType', models.CharField(max_length=50)),
                ('relevance', models.DecimalField(max_digits=10, decimal_places=6)),
                ('count', models.IntegerField(default=0)),
                ('text', models.CharField(max_length=50)),
                ('sentimentType', models.CharField(max_length=25)),
                ('sentimentScore', models.DecimalField(max_digits=10, decimal_places=6)),
            ],
        ),
        migrations.CreateModel(
            name='journalEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('created', models.DateTimeField()),
                ('entry', models.TextField()),
                ('sentimentType', models.CharField(max_length=25)),
                ('sentimentScore', models.DecimalField(max_digits=10, decimal_places=6)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='keywords',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=50)),
                ('relevance', models.DecimalField(max_digits=10, decimal_places=6)),
                ('sentimentType', models.CharField(max_length=25)),
                ('sentimentScore', models.DecimalField(max_digits=10, decimal_places=6)),
                ('entry', models.ForeignKey(to='journal.journalEntry')),
            ],
        ),
        migrations.AddField(
            model_name='entities',
            name='entry',
            field=models.ForeignKey(to='journal.journalEntry'),
        ),
    ]

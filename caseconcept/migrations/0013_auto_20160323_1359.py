# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('caseconcept', '0012_auto_20160322_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemaspect',
            name='summary',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='problemaspectsituation',
            unique_together=set([('problem', 'situation', 'thoughts_and_feelings', 'reaction', 'distress_level')]),
        ),
        migrations.RemoveField(
            model_name='problemaspectsituation',
            name='summary',
        ),
    ]

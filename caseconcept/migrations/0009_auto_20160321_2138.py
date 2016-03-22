# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('caseconcept', '0008_problemaspectsituation_summary'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='problemaspectsituation',
            unique_together=set(
                [('problem', 'summary', 'situation', 'thoughts_and_feelings', 'reaction', 'distress_level')]),
        ),
    ]

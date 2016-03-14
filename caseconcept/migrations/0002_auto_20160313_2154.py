# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('caseconcept', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemaspectsituation',
            name='distress_level',
            field=models.SmallIntegerField(
                choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
        ),
    ]

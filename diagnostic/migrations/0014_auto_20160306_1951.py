# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic', '0013_auto_20160306_1951'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='problemgoalranking',
            unique_together=set([]),
        ),
    ]

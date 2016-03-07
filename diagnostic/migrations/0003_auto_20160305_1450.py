# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic', '0002_problemaspect_problemaspectsituations'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProblemAspectSituations',
            new_name='ProblemAspectSituation',
        ),
    ]

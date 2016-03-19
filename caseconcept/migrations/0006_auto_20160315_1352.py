# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('caseconcept', '0005_auto_20160315_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemaspect',
            name='text',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]

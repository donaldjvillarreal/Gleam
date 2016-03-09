# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caseconcept', '0006_auto_20160309_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemaspect',
            name='frequency',
            field=models.SmallIntegerField(choices=[(0, b'Every day'), (1, b'Once a week'), (2, b'Once a month'), (3, b'Every few months')]),
        ),
        migrations.AlterField(
            model_name='problemaspect',
            name='severity',
            field=models.SmallIntegerField(choices=[(0, b'Very Minor'), (1, b'Minor'), (2, b'Moderate'), (3, b'Serious'), (4, b'Very Serious')]),
        ),
    ]

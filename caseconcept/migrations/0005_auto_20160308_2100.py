# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caseconcept', '0004_auto_20160307_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicecal',
            name='WeekdayTime',
            field=models.CharField(max_length=5, choices=[(b'10000', b'1'), (b'20000', b'2'), (b'30000', b'3'), (b'40000', b'4'), (b'50000', b'5'), (b'60000', b'6'), (b'70000', b'7')]),
        ),
    ]

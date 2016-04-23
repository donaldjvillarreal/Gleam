# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('authenticate', '0014_auto_20160421_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='therapist',
            name='user',
            field=models.OneToOneField(to='authenticate.UserProfile'),
        ),
    ]

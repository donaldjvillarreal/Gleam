# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('authenticate', '0015_auto_20160422_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='client',
            new_name='user_profile',
        ),
        migrations.RenameField(
            model_name='therapist',
            old_name='user',
            new_name='user_profile',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_therapist',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic', '0007_remove_problemaspect_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemaspect',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

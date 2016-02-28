# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0020_auto_20150821_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AlterField(
            model_name='answer',
            name='user_data',
            field=models.ForeignKey(to='authenticate.UserProfile'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_data',
            field=models.ForeignKey(to='authenticate.UserProfile'),
        ),
        migrations.AlterField(
            model_name='question',
            name='user_data',
            field=models.ForeignKey(to='authenticate.UserProfile'),
        ),
        migrations.AlterField(
            model_name='qvoter',
            name='user',
            field=models.ForeignKey(to='authenticate.UserProfile'),
        ),
        migrations.AlterField(
            model_name='voter',
            name='user',
            field=models.ForeignKey(to='authenticate.UserProfile'),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]

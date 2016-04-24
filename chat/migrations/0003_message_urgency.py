# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('chat', '0002_message_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='urgency',
            field=models.CharField(blank=True, max_length=50, null=True,
                                   choices=[(b'minor', b'Minor'), (b'moderate', b'Moderate'),
                                            (b'important', b'Important'), (b'emergency', b'Emergency')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Therapist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('practice', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=2)),
                ('zip', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.IntegerField(default=0)),
                ('gender', models.CharField(default='U', max_length=1,
                                            choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Prefer Not to Answer')])),
                ('picture', models.ImageField(null=True, upload_to='static/profile_images', blank=True)),
                ('dob', models.DateField()),
                ('timezone', models.IntegerField(default=0)),
                ('phone', models.CharField(blank=True, max_length=10, null=True, validators=[
                    django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$',
                                                          message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('subscribed', models.BooleanField(default=False)),
                ('is_therapist', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='therapist',
            name='user_profile',
            field=models.OneToOneField(to='authenticate.UserProfile'),
        ),
        migrations.AddField(
            model_name='client',
            name='therapist',
            field=models.ForeignKey(to='authenticate.Therapist'),
        ),
        migrations.AddField(
            model_name='client',
            name='user_profile',
            field=models.OneToOneField(to='authenticate.UserProfile'),
        ),
    ]

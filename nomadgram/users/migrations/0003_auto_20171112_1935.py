# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-12 10:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171112_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='folloing',
            field=models.ManyToManyField(related_name='_user_folloing_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='follower',
            field=models.ManyToManyField(related_name='_user_follower_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-29 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_auto_20160429_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_receiver',
            field=models.BooleanField(default=True, verbose_name='Is This User Receiver Or Sender'),
        ),
    ]

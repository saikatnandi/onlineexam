# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-29 11:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_message_is_receiver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='url',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-24 02:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_notice_notice_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice_topic',
            old_name='notice_topic_text',
            new_name='notice_topic_text2',
        ),
    ]

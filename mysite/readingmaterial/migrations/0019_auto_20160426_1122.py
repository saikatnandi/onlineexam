# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-26 11:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readingmaterial', '0018_auto_20160426_1035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentmarkedmcq',
            name='content',
        ),
        migrations.RemoveField(
            model_name='contentmarkedmcq',
            name='mcq_question',
        ),
        migrations.RemoveField(
            model_name='contentmarkedmcq',
            name='user',
        ),
        migrations.DeleteModel(
            name='ContentMarkedMcq',
        ),
    ]

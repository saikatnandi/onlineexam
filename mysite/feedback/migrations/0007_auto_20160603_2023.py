# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-03 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0006_auto_20160603_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='report_text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 03:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('readingmaterial', '0015_remove_contentmarkedmcq_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentmarkedmcq',
            name='content',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='readingmaterial.ReadingContent'),
        ),
    ]

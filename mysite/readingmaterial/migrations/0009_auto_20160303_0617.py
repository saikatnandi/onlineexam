# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readingmaterial', '0008_readingcontent_mcq_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='readingcontent',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='images/content/'),
        ),
        migrations.AddField(
            model_name='readingcontent',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='images/content/'),
        ),
    ]

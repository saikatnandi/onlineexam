# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-27 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0004_auto_20160427_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription_plan',
            name='no_of_random_question',
            field=models.IntegerField(default=0, verbose_name='No Of Random Question'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-07 03:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0007_auto_20160307_0337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload_question_set_from_excel',
            old_name='content',
            new_name='question_set',
        ),
    ]
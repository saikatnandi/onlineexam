# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-22 05:57
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160309_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_body2',
            field=ckeditor.fields.RichTextField(default='alamin'),
            preserve_default=False,
        ),
    ]

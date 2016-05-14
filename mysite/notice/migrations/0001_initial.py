# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-24 02:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_text', models.TextField(max_length=200, verbose_name='Notice ')),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='Publishing Date: ')),
                ('edit_date', models.DateTimeField(blank=True, null=True, verbose_name='Editing Date: ')),
                ('notice_image1', models.ImageField(blank=True, null=True, upload_to='images/notice/')),
                ('notice_image2', models.ImageField(blank=True, null=True, upload_to='images/notice/')),
                ('notice_image3', models.ImageField(blank=True, null=True, upload_to='images/notice/')),
                ('notice_file1', models.FileField(blank=True, null=True, upload_to='files/notice/')),
                ('notice_file2', models.FileField(blank=True, null=True, upload_to='files/notice/')),
                ('notice_file3', models.FileField(blank=True, null=True, upload_to='files/notice/')),
            ],
            options={
                'verbose_name': 'Notice',
            },
        ),
        migrations.CreateModel(
            name='Notice_Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_topic_text', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Notice Topic List',
            },
        ),
        migrations.AddField(
            model_name='notice',
            name='notice_topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notice.Notice_Topic'),
        ),
        migrations.AddField(
            model_name='notice',
            name='uploader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

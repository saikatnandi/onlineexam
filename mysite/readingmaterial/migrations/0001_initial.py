# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 07:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReadingContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_title', models.CharField(max_length=200)),
                ('content_body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SubTopic1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtopic1_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SubTopic2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtopic2_text', models.CharField(max_length=200)),
                ('subtopic1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readingmaterial.SubTopic1')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='subtopic1',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readingmaterial.Topic'),
        ),
        migrations.AddField(
            model_name='readingcontent',
            name='subtopic1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='readingmaterial.SubTopic1'),
        ),
        migrations.AddField(
            model_name='readingcontent',
            name='subtopic2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='readingmaterial.SubTopic2'),
        ),
    ]

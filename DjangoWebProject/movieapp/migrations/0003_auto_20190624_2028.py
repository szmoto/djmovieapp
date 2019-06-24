# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-24 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_auto_20190624_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='filehd',
            field=models.IntegerField(choices=[(0, '1080P'), (1, '720P'), (2, '720P/1080P')], default=0, verbose_name='高清类别'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.IntegerField(choices=[(0, '国语'), (1, '外语')], default=0, verbose_name='电影语言'),
        ),
    ]
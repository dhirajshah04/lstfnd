# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostfoundmgmt', '0012_auto_20171120_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=120, unique=True),
        ),
    ]
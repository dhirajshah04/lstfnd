# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-01 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostfoundmgmt', '0013_auto_20171129_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='contact',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]

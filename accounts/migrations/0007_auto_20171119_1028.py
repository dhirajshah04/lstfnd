# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 10:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20171119_1019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='City',
            new_name='city',
        ),
    ]

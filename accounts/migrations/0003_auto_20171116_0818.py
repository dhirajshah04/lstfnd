# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 08:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20171116_0749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userregister',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserRegister',
        ),
    ]

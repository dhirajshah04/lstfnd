# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostfoundmgmt', '0010_auto_20171114_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostfoundmgmt', '0007_auto_20171113_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='zone',
            field=models.CharField(choices=[('select_zone', 'select_zone'), ('koshi', 'koshi'), ('sagarmatha', 'sagarmatha'), ('Mechi', 'Mechi'), ('Janakpur', 'Janakpur'), ('Bagmati', 'Bagmati'), ('Narayani', 'Narayani'), ('Gandaki', 'Gandaki'), ('Dhawalagiri', 'Dhawalagiri'), ('Lumbini', 'Lumbini'), ('Rapti', 'Rapti'), ('Bheri', 'Bheri'), ('Karnali', 'Karnali'), ('Seti', 'Seti'), ('Mahakali', 'Mahakali')], default='select_zone', max_length=25),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique_for_date='published_date'),
        ),
    ]

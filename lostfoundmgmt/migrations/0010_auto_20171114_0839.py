# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostfoundmgmt', '0009_auto_20171114_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='media/default-img.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='lost_or_found',
            field=models.CharField(choices=[('', 'Select'), ('LOST', 'Lost'), ('FOUND', 'Found')], max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='zone',
            field=models.CharField(choices=[('', 'Select Zone'), ('koshi', 'koshi'), ('sagarmatha', 'sagarmatha'), ('Mechi', 'Mechi'), ('Janakpur', 'Janakpur'), ('Bagmati', 'Bagmati'), ('Narayani', 'Narayani'), ('Gandaki', 'Gandaki'), ('Dhawalagiri', 'Dhawalagiri'), ('Lumbini', 'Lumbini'), ('Rapti', 'Rapti'), ('Bheri', 'Bheri'), ('Karnali', 'Karnali'), ('Seti', 'Seti'), ('Mahakali', 'Mahakali')], max_length=25),
        ),
    ]

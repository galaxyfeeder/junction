# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20161126_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='stop',
            name='people_leaving',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stop',
            name='travel_time',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

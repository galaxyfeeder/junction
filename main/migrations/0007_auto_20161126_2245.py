# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20161126_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='people_waiting',
        ),
        migrations.AddField(
            model_name='stop',
            name='people_waiting',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
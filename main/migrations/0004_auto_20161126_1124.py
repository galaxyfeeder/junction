# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_bus_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='code',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='code',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]

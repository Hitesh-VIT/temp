# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 14:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20170217_1111'),
        ('links', '0002_auto_20170423_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='categories.Category'),
            preserve_default=False,
        ),
    ]

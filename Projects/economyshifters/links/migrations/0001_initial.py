# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 19:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referral_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('default_referral', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User_refferal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Main_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_user', to=settings.AUTH_USER_MODEL, unique=True)),
                ('Referred_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='link_info',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='links.Links'),
        ),
        migrations.AddField(
            model_name='link_info',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

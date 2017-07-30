# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 04:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoreInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spu', models.CharField(max_length=200)),
                ('loyaltyurl', models.CharField(max_length=200)),
                ('store_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WifiGuest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=300)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('honeypot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeinfo',
            name='loyaltyurl',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='storeinfo',
            name='spu',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

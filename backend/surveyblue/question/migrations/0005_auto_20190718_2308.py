# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-19 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_auto_20190718_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]

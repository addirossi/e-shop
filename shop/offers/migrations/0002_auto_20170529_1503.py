# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='discount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-06 19:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20170606_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Subcategory', verbose_name='Subcategory'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-01 13:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20190401_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sections',
        ),
    ]
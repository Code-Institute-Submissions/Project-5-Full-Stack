# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-09 20:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catergories', '0002_auto_20190409_2031'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sizes',
            new_name='Size',
        ),
    ]
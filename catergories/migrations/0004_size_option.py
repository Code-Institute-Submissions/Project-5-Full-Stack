# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-09 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catergories', '0003_auto_20190409_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='option',
            field=models.CharField(blank=True, choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], default=0, max_length=5, null=True),
        ),
    ]

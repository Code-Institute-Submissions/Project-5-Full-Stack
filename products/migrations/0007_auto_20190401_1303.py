# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-01 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catergories', '0005_auto_20190321_0049'),
        ('products', '0006_auto_20190401_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='catergories',
            field=models.CharField(blank=True, choices=[('Men', 'Mens'), ('Women', 'Womens'), ('Unisex', 'Unisexs'), ('Extra', 'Extras')], default=0, max_length=8),
        ),
        migrations.RemoveField(
            model_name='product',
            name='sections',
        ),
        migrations.AddField(
            model_name='product',
            name='sections',
            field=models.ManyToManyField(to='catergories.Men'),
        ),
    ]
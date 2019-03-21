# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-21 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catergories', '0004_auto_20190320_1244'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Catergorie',
        ),
        migrations.AlterField(
            model_name='extra',
            name='image',
            field=models.ImageField(upload_to='cats/extra'),
        ),
        migrations.AlterField(
            model_name='men',
            name='image',
            field=models.ImageField(upload_to='cats/mens'),
        ),
        migrations.AlterField(
            model_name='unisex',
            name='image',
            field=models.ImageField(upload_to='cats/unisex'),
        ),
        migrations.AlterField(
            model_name='women',
            name='image',
            field=models.ImageField(upload_to='cats/womens'),
        ),
    ]
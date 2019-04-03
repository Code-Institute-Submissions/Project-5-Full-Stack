# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-03 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catergories', '0005_auto_20190321_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='extra',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catergories.Extra'),
        ),
        migrations.AddField(
            model_name='men',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catergories.Men'),
        ),
        migrations.AddField(
            model_name='unisex',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catergories.Unisex'),
        ),
        migrations.AddField(
            model_name='women',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catergories.Women'),
        ),
    ]
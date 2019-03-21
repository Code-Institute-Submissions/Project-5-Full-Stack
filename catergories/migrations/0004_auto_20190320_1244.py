# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-20 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catergories', '0003_extra_men_women'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unisex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=254)),
                ('image', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name': 'A Unisexs Catergory',
                'verbose_name_plural': 'Unisexs',
            },
        ),
        migrations.AlterModelOptions(
            name='extra',
            options={'verbose_name': 'A Extras Catergory', 'verbose_name_plural': 'Extras'},
        ),
        migrations.AlterModelOptions(
            name='men',
            options={'verbose_name': 'A Mens Catergory', 'verbose_name_plural': 'Mens'},
        ),
        migrations.AlterModelOptions(
            name='women',
            options={'verbose_name': 'A Womens Catergory', 'verbose_name_plural': 'Womens'},
        ),
    ]
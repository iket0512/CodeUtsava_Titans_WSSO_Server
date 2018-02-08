# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-03 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20180203_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitationdata',
            name='latitude',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=15),
        ),
        migrations.AddField(
            model_name='habitationdata',
            name='longitude',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='elementdata',
            name='permissible_limit_high',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='elementdata',
            name='permissible_limit_low',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-15 23:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0030_auto_20171115_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productiondata',
            name='well',
            field=models.ForeignKey(blank=True, db_column='well_tag_number', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.Well'),
        ),
        migrations.AlterField(
            model_name='well',
            name='development_method',
            field=models.ForeignKey(blank=True, db_column='development_method_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.DevelopmentMethod', verbose_name='Developed By'),
        ),
    ]

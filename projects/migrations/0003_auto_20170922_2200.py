# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-22 16:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20170922_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='owner',
            new_name='team_name',
        ),
    ]

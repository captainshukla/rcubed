# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-22 15:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='added_by',
            new_name='owner',
        ),
    ]

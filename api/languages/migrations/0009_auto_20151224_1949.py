# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-24 19:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0008_auto_20151224_1948'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorial',
            old_name='homepage_url',
            new_name='tutorial_url',
        ),
    ]

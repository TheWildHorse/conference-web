# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 10:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20160502_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='hero_type',
        ),
        migrations.RemoveField(
            model_name='page',
            name='title_in_hero',
        ),
    ]

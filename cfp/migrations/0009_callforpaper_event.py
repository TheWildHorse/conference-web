# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-08 14:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20161008_1644'),
        ('cfp', '0008_auto_20160910_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='callforpaper',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
            preserve_default=False,
        ),
    ]
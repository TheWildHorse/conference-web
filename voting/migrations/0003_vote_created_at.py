# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-11 10:08


import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0002_auto_20150813_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 9, 11, 10, 8, 35, 118966, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

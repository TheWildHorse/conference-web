# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-08 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0005_ticket_tshirt_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='used_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
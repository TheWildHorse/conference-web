# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 18:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0003_auto_20161008_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_talk_updates', models.BooleanField(help_text='If set to false, users will no longer be able to update talk descriptions.')),
                ('community_vote_enabled', models.BooleanField(help_text='Enable the community vote page.')),
                ('active_event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='events.Event')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

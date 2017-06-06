# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 13:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cfp', '0014_auto_20170605_1545'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveSmallIntegerField()),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='committee_votes', to='cfp.PaperApplication')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='committee_votes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('user', 'application')]),
        ),
    ]

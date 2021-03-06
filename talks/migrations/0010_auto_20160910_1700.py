# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-10 15:00


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usergroups', '0005_voteaudit'),
        ('sponsors', '0008_sponsor_order'),
        ('talks', '0009_talk_rate_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talk',
            name='is_sponsored',
        ),
        migrations.AddField(
            model_name='talk',
            name='sponsor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sponsored_talks', to='sponsors.Sponsor'),
        ),
        migrations.AddField(
            model_name='talk',
            name='usergroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='chosen_talks', to='usergroups.UserGroup'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='application',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='talk', to='cfp.PaperApplication'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='co_presenter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='co_talks', to='cfp.Applicant'),
        ),
    ]

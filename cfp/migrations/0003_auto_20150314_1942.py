# -*- coding: utf-8 -*-


from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('cfp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callforpaper',
            name='description',
            field=tinymce.models.HTMLField(),
            preserve_default=True,
        ),
    ]

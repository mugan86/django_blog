# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='photo_url',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='source',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='source_title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]

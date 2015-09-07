# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_auto_20150907_0841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventtype',
            name='location',
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(default=b'Bilbao', to='blog.Location'),
        ),
    ]

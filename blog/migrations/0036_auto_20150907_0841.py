# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0035_auto_20150907_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtype',
            name='location',
            field=models.ForeignKey(default=b'Bilbao', to='blog.Location'),
        ),
    ]

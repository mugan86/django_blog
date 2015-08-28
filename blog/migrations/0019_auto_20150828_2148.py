# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20150828_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]

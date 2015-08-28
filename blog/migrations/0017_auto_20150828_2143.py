# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20150828_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='active',
        ),
        migrations.RemoveField(
            model_name='post',
            name='the_most_important',
        ),
    ]

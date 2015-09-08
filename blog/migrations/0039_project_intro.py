# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0038_auto_20150907_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='intro',
            field=models.CharField(default='', max_length=200, verbose_name=b'Introducci\xc3\xb3n'),
            preserve_default=False,
        ),
    ]

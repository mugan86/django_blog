# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20150826_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]

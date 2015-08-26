# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20150826_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='finish',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='start_project_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

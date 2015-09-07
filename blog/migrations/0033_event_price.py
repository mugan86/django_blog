# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_event_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='price',
            field=models.FloatField(default=0, verbose_name=b'Precio', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10000000)]),
        ),
    ]

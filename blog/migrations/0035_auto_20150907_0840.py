# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtype',
            name='location',
            field=models.ForeignKey(default=b'', to='blog.Location'),
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.FloatField(default=0, verbose_name=b'Latitud', validators=[django.core.validators.MinValueValidator(-1000000), django.core.validators.MaxValueValidator(10000000)]),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.FloatField(default=0, verbose_name=b'Longitud', validators=[django.core.validators.MinValueValidator(-100000), django.core.validators.MaxValueValidator(10000000)]),
        ),
    ]

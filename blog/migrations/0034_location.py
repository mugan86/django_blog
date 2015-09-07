# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_event_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=100)),
                ('region_eus', models.CharField(max_length=100)),
                ('longitude', models.FloatField(default=0, verbose_name=b'Longitud', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10000000)])),
                ('latitude', models.FloatField(default=0, verbose_name=b'Latitud', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10000000)])),
                ('region_ca', models.CharField(max_length=100)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]

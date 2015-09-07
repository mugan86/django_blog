# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_auto_20150903_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('name', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=150)),
                ('free', models.BooleanField(default=True)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Fecha publicaci\xc3\xb3n')),
                ('category', models.ForeignKey(to='blog.Category')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20150828_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collaboration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(default='', max_length=200)),
                ('img', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('add_data', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(to='blog.Category')),
            ],
        ),
    ]

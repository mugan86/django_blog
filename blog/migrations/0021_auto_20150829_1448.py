# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_collaboration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
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
        migrations.CreateModel(
            name='FriendType',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('add_data', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='collaboration',
            name='category',
        ),
        migrations.DeleteModel(
            name='Collaboration',
        ),
    ]

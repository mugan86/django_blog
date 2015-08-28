# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20150827_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostType',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', ckeditor.fields.RichTextField()),
                ('active', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.ForeignKey(to='blog.PostType', default=''),
            preserve_default=False,
        ),
    ]

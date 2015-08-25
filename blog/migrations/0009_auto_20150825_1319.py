# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category1',
            field=models.ForeignKey(related_name='category1', default='General', to='blog.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='category2',
            field=models.ForeignKey(related_name='category2', default='General', to='blog.Category'),
            preserve_default=False,
        ),
    ]

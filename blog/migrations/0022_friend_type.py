# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20150829_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='type',
            field=models.ForeignKey(to='blog.FriendType', default='Links interesantes'),
            preserve_default=False,
        ),
    ]

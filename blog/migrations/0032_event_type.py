# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_eventtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(related_name='Tipo', default=b'Carrera', to='blog.EventType'),
        ),
    ]

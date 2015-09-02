# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20150902_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='logotype',
            field=models.CharField(default=datetime.datetime(2015, 9, 2, 14, 28, 6, 149490, tzinfo=utc), verbose_name='Logotipo', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(verbose_name='Descripción', max_length=250),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(verbose_name='Nombre', max_length=150),
        ),
        migrations.AlterField(
            model_name='event',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha publicación'),
        ),
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.CharField(verbose_name='Más información', max_length=150),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20150901_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='active',
            field=models.BooleanField(default=True, verbose_name=b'\xc2\xbfActivo?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Fecha de creaci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=200, verbose_name=b'Descripci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Fecha de publicaci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='post',
            name='source',
            field=models.CharField(max_length=250, verbose_name=b'Fuente'),
        ),
        migrations.AlterField(
            model_name='post',
            name='source_title',
            field=models.CharField(max_length=200, verbose_name=b'T\xc3\xadtulo fuente'),
        ),
        migrations.AlterField(
            model_name='post',
            name='the_most_important',
            field=models.BooleanField(default=False, verbose_name=b'\xc2\xbfDestacado?'),
        ),
    ]

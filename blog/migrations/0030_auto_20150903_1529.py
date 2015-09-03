# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_auto_20150902_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Fecha de creaci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(verbose_name=b'Descripci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='category',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Fecha de publicaci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=200, serialize=False, verbose_name=b'T\xc3\xadtulo', primary_key=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=100, verbose_name=b'Correo electr\xc3\xb3nico'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=250, verbose_name=b'Descripci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='event',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Fecha publicaci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.CharField(max_length=150, verbose_name=b'M\xc3\xa1s informaci\xc3\xb3n'),
        ),
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
            name='source_title',
            field=models.CharField(max_length=200, verbose_name=b'T\xc3\xadtulo fuente'),
        ),
        migrations.AlterField(
            model_name='post',
            name='the_most_important',
            field=models.BooleanField(default=False, verbose_name=b'\xc2\xbfDestacado?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name=b'T\xc3\xadtulo'),
        ),
        migrations.AlterField(
            model_name='posttype',
            name='active',
            field=models.BooleanField(default=False, verbose_name=b'\xc2\xbfActivo?'),
        ),
        migrations.AlterField(
            model_name='posttype',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Fecha de creaci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='posttype',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name=b'Descripci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='posttype',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Fecha de publicaci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='project',
            name='active',
            field=models.BooleanField(default=True, verbose_name=b'\xc2\xbfActivo?'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name=b'Descripci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='project',
            name='finish',
            field=models.BooleanField(default=False, verbose_name=b'\xc2\xbfFinalizado'),
        ),
        migrations.AlterField(
            model_name='project',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Fecha de publicaci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='project',
            name='source_title',
            field=models.CharField(max_length=200, verbose_name=b'T\xc3\xadtulo de la fuente'),
        ),
    ]

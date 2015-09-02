# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20150901_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=150, verbose_name='Nombre')),
                ('description', models.TextField(max_length=250, verbose_name='Descripción')),
                ('url', models.TextField(max_length=150, verbose_name='Más información')),
                ('celebrate_data', models.DateTimeField(verbose_name='Fecha y Hora')),
                ('published_date', models.DateTimeField(verbose_name='Fecha publicación')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(verbose_name='Fecha de creación', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='category',
            name='published_date',
            field=models.DateTimeField(verbose_name='Fecha de publicación', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=200, primary_key=True, verbose_name='Título', serialize=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=100, verbose_name='Correo electrónico'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(verbose_name='Mensaje'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='received_date',
            field=models.DateTimeField(verbose_name='Recibido', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='active',
            field=models.BooleanField(verbose_name='¿Activo?', default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(verbose_name='Fecha de creación', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=200, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(verbose_name='Fecha de publicación', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='source',
            field=models.CharField(max_length=250, verbose_name='Fuente'),
        ),
        migrations.AlterField(
            model_name='post',
            name='source_title',
            field=models.CharField(max_length=200, verbose_name='Título fuente'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='post',
            name='the_most_important',
            field=models.BooleanField(verbose_name='¿Destacado?', default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='posttype',
            name='active',
            field=models.BooleanField(verbose_name='¿Activo?', default=False),
        ),
        migrations.AlterField(
            model_name='posttype',
            name='created_date',
            field=models.DateTimeField(verbose_name='Fecha de creación', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='posttype',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='posttype',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, verbose_name='Nombre', serialize=False),
        ),
        migrations.AlterField(
            model_name='posttype',
            name='published_date',
            field=models.DateTimeField(verbose_name='Fecha de publicación', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='active',
            field=models.BooleanField(verbose_name='¿Activo?', default=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='project',
            name='finish',
            field=models.BooleanField(verbose_name='¿Finalizado', default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='project',
            name='photo_url',
            field=models.CharField(max_length=255, verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='project',
            name='published_date',
            field=models.DateTimeField(verbose_name='Fecha de publicación', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='source',
            field=models.CharField(max_length=250, verbose_name='Fuente'),
        ),
        migrations.AlterField(
            model_name='project',
            name='source_title',
            field=models.CharField(max_length=200, verbose_name='Título de la fuente'),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_project_date',
            field=models.DateTimeField(verbose_name='Fecha de inicio', default=django.utils.timezone.now),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-05 06:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servirace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryzer_kodea', models.CharField(max_length=69, primary_key=True, serialize=False, verbose_name='Code')),
                ('cat_basque', models.CharField(max_length=50, verbose_name='Category (Basque)')),
                ('cat_spanish', models.CharField(max_length=50, verbose_name='Category (Spanish)')),
                ('cat_english', models.CharField(max_length=50, verbose_name='Category (English)')),
                ('image_url', models.CharField(blank=True, max_length=150, verbose_name='Image Url')),
                ('cat_ca', models.CharField(max_length=50, verbose_name='Category (Catala)')),
            ],
        ),
        migrations.AlterField(
            model_name='lasterketa',
            name='finish_herri_kodea',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='town_finish', to='servirace.Herria'),
        ),
        migrations.AlterField(
            model_name='lasterketa',
            name='finish_latitudea',
            field=models.CharField(blank=True, max_length=15, verbose_name='Finish Latitude'),
        ),
        migrations.AlterField(
            model_name='lasterketa',
            name='finish_longitudea',
            field=models.CharField(blank=True, max_length=15, verbose_name='Finish Longitude'),
        ),
        migrations.AlterField(
            model_name='lasterketa',
            name='route',
            field=models.CharField(blank=True, max_length=20, verbose_name='Route ID'),
        ),
        migrations.AlterField(
            model_name='lasterketa',
            name='short_url',
            field=models.CharField(blank=True, max_length=100, verbose_name='Short URL'),
        ),
    ]

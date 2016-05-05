from __future__ import unicode_literals

from django.db import models

# Create your models here.
# -*- encoding: utf-8 -*-
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Herria(models.Model):
    herri_kodea = models.CharField('Code', primary_key=True, max_length=50)
    izena = models.CharField('Name', max_length=50)
    probintzia = models.CharField('Province', max_length=50)
    autonomi_erkidegoa = models.CharField('Autonomy (ES)', max_length=100)
    autonomi_erkidegoa_eus = models.CharField('Autonomy (EU)', max_length=100)
    longitudea = models.CharField('Longitude', max_length=15)
    latitudea = models.CharField('Latitude', max_length=15)
    autonomi_erkidegoa_ca = models.CharField('Autonomy (CA)', max_length=100)
    #in python 3 set __str__
    def __unicode__(self):
        return u'%s' % self.izena
class Organizator(models.Model):
    code = models.CharField('Code', primary_key=True, max_length=100)
    name = models.CharField('Name', max_length=256)
    tlf = models.CharField('Telephone 1', max_length=30);
    tlf2 = models.CharField('Telephone 2', max_length=30);
    twitter = models.CharField('Twitter', max_length=50);
    facebook = models.CharField('Facebook', max_length=150);
    email = models.CharField('E-Mail', max_length=256);

    def __unicode__(self):
        return u'%s' % self.name

class Lasterketa(models.Model):
    laster_kodea = models.CharField('Code', primary_key=True, max_length=50)
    izena = models.CharField('Name', max_length=256)
    edizio_kop = models.IntegerField('Edition');
    distantzia = models.CharField('Distance', max_length=6);
    desnibela = models.CharField('Climb', max_length=5);
    longitudea = models.CharField('Longitude', max_length=15)
    latitudea = models.CharField('Latitude', max_length=15)
    route = models.CharField('Route ID', max_length=20, blank=True);
    route_source = models.CharField('Route Source', max_length=30);
    noiz = models.DateField("Data", default = timezone.now)
    start_time = models.TimeField("Start Time", default = timezone.now)
    web = models.CharField('Web', max_length=256)
    video = models.BooleanField('Video', default=False)
    mota = models.CharField('Type', max_length=50)
    herri_kodea = models.ForeignKey('Herria', related_name='town')
    gehitua = models.DateTimeField('Add Data', default=timezone.now)
    circle_circuit = models.BooleanField('Circle circuit?', default=True)
    finish_herri_kodea = models.ForeignKey('Herria', related_name='town_finish', blank=True);
    finish_longitudea = models.CharField('Finish Longitude', max_length=15, blank=True)
    finish_latitudea = models.CharField('Finish Latitude', max_length=15, blank=True)
    short_url = models.CharField('Short URL', max_length=100, blank=True)
    organizator = models.ForeignKey('Organizator')

    def __unicode__(self):
        return u'%s' % self.izena

class Category(models.Model):
    categoryzer_kodea = models.CharField('Code', primary_key=True, max_length=69)
    cat_basque = models.CharField('Category (Basque)', max_length=50)
    cat_spanish = models.CharField('Category (Spanish)', max_length=50)
    cat_english = models.CharField('Category (English)', max_length=50)
    image_url = models.CharField('Image Url', max_length=150, blank=True)
    cat_ca = models.CharField('Category (Catala)', max_length=50)

"""class Zerbitzua(models.Model):
    zer_kodea = models.CharField('Code', primary_key=True, max_length=69)
    name = models.TextField('Name')
    categoryzer_kodea = models.ForeignKey('Category')"""
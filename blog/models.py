# -*- encoding: utf-8 -*-
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator

"""
def __str__(self) instead of def __unicode__(self) in python3. Set Unicode and no error (in python2 must be __unicode__)
"""

class Post(models.Model):
    """
    Post propert
    """
    author = models.ForeignKey('auth.User')
    title = models.CharField('Título', max_length=200)
    description = models.CharField('Descripción', max_length=200)
    text = RichTextField('Contenido')
    source = models.CharField('Fuente', max_length=250)
    source_title = models.CharField('Título fuente', max_length=200)
    category1 = models.ForeignKey('Category', related_name='category1')
    category2 = models.ForeignKey('Category', related_name='category2')
    post_type = models.ForeignKey('PostType');
    the_most_important = models.BooleanField('¿Destacado?', default=False)
    active = models.BooleanField('¿Activo?', default=True)
    created_date = models.DateTimeField(
                'Fecha de creación' , default=timezone.now)
    published_date = models.DateTimeField(
                'Fecha de publicación' , default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return u'%s' % self.title

class PostType(models.Model):
    """Manage post type data to classified in different types (blog, videos, articles,...)"""

    name = models.CharField('Nombre', max_length=100, primary_key=True)
    description = RichTextField('Descripción')
    active = models.BooleanField('¿Activo?', default=False)
    created_date = models.DateTimeField('Fecha de creación',
                default=timezone.now)
    published_date = models.DateTimeField('Fecha de publicación',
                default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return u'%s' % self.name

class Category(models.Model):
    """
    Category propert
    """
    title = models.CharField('Título', max_length=200, primary_key=True)
    description = models.TextField("Descripción")
    created_date = models.DateTimeField('Fecha de creación',
                default=timezone.now)
    published_date = models.DateTimeField('Fecha de publicación',
                default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return u'%s' % self.title

class Contact(models.Model):
    """
    Contact propert
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("Nombre", max_length=100)
    email = models.CharField("Correo electrónico" , max_length=100)
    message = models.TextField("Mensaje")
    received_date = models.DateTimeField('Recibido',
                default=timezone.now)

    def publish(self):
        self.received_date = timezone.now()
        self.save()

    def __unicode__(self):
        return u'%s' % self.name

class Project(models.Model):
    """
    Project propert
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=150)
    intro = models.CharField('Introducción', max_length=200)
    description = RichTextField('Descripción')
    category = models.ForeignKey('Category')
    source = models.CharField('Fuente', max_length=250)
    source_title = models.CharField('Título de la fuente', max_length=200)
    photo_url = models.CharField('Imagen', max_length=255)
    finish = models.BooleanField('¿Finalizado', default=False)
    active = models.BooleanField('¿Activo?', default=True)
    start_project_date = models.DateTimeField('Fecha de inicio',
                default=timezone.now)
    published_date = models.DateTimeField('Fecha de publicación',
                default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return u'%s' % self.name

class Friend(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=200, default="")
    category = models.ForeignKey('Category')
    img = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    type = models.ForeignKey('FriendType')
    add_data = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.add_data = timezone.now()
        self.save()

    def __unicode__(self):
        return u'%s' % self.name

class FriendType(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    add_data = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.add_data = timezone.now()
        self.save()

    def __unicode__(self):
        return u'%s' % self.name

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=150)
    description = models.CharField('Descripción', max_length=250)
    url = models.CharField('Más información', max_length=150)
    type = models.ForeignKey("EventType", related_name="Tipo", default="Carrera")
    logotype = models.CharField('Logotipo', max_length=200)
    price = models.FloatField("Precio", validators = [MinValueValidator(0.0), MaxValueValidator(10000000)], default=0)
    location = models.ForeignKey('Location')
    celebrate_data = models.DateTimeField("Fecha y Hora")
    published_date = models.DateTimeField("Fecha publicación", default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return u'%s' % self.name

class EventType(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    description = models.CharField(max_length=150)
    category = models.ForeignKey('Category')
    free = models.BooleanField(default=True)
    published_date = models.DateTimeField("Fecha publicación", default = timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return u'%s' % self.name

class Location(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    region = models.CharField(max_length=100)
    region_eus = models.CharField(max_length=100)
    longitude = models.FloatField("Longitud", validators = [MinValueValidator(-100000), MaxValueValidator(10000000)], default=0)
    latitude = models.FloatField("Latitud", validators = [MinValueValidator(-1000000), MaxValueValidator(10000000)], default=0)
    region_ca= models.CharField(max_length=100)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return u'%s' % self.name


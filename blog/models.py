from django.db import models
from django.utils import timezone

class Post(models.Model):
    """
    Post propert
    """
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    text = models.TextField()
    source = models.CharField(max_length=250)
    source_title = models.CharField(max_length=200)
    category = models.ForeignKey('Category')
    created_date = models.DateTimeField(
                default=timezone.now)
    published_date = models.DateTimeField(
                default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Category(models.Model):
    """
    Category propert
    """
    title = models.CharField(max_length=200, primary_key=True)
    description = models.TextField()
    created_date = models.DateTimeField(
                default=timezone.now)
    published_date = models.DateTimeField(
                default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Contact(models.Model):
    """
    Contact propert
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()
    received_date = models.DateTimeField(
                default=timezone.now)

    def publish(self):
        self.received_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

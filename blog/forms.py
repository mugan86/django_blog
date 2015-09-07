# -*- coding: utf-8 -*-
from django import forms
from .models import Post, Contact, Event

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        # Fields to show in form
        fields = ('title', 'description', 'text', 'category1', 'category2','post_type' , 'source', 'source_title')

    #Validate post title length minimum 5 characters
    def clean_title(self):
        diccionario_limpio = self.cleaned_data

        title = diccionario_limpio.get('title')

        if len(title) < 5:
            raise forms.ValidationError("El título debe contener más de cinco carácteres")


        return title

    #Validate post title length minimum 5 characters
    def clean_description(self):
        diccionario_limpio = self.cleaned_data

        description = diccionario_limpio.get('description')

        if len(description) < 10:
            raise forms.ValidationError("La descripción debe contener más de 10 carácteres")

        return description

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        # Fields to show in form
        fields = ('name', 'description', 'url', 'type', 'logotype','price' , 'location', 'celebrate_data')


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        # Fields to show in form
        fields = ('name', 'email', 'message', )

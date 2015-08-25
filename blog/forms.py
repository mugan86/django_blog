from django import forms
from .models import Post
from .models import Contact

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        # Fields to show in form
        fields = ('title', 'description', 'text')

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        # Fields to show in form
        fields = ('name', 'email', 'message', )

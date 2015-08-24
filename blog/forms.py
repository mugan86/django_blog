from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        # Fields to show in form
        fields = ('title', 'description', 'text')

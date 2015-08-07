from django.contrib import admin
from .models import Post
from .models import Category

admin.site.register(Post)
#Add create model in admin site to show
admin.site.register(Category)
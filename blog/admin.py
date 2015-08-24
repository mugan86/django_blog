from django.contrib import admin
from .models import Post
from .models import Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'description', 'created_date','published_date', )
    
admin.site.register(Post, PostAdmin)
#Add create model in admin site to show
admin.site.register(Category)
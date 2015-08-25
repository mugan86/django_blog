from django.contrib import admin
from .models import Post
from .models import Category
from .models import Contact


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'description', 'created_date','published_date', )

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','received_date', )

admin.site.register(Post, PostAdmin)

#Add create model in admin site to show
admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)

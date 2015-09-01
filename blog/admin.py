# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Post
from .models import PostType
from .models import Category
from .models import Contact
from .models import Project
from .models import Friend
from .models import FriendType


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'description', 'text', 'active' , 'category1', 'category2', 'published_date', )
    list_filter = ('author', 'published_date')
    ordering = ('-published_date',)
    search_fields = ('title',)

class PostTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'active', 'created_date','published_date', )
    list_filter = ('name', 'published_date', 'active')
    ordering = ('-published_date',)
    search_fields = ('description',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_date','published_date',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','received_date', )

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'start_project_date', 'active', 'finish', 'published_date')

class FriendAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'img', 'url', 'active', 'type')
    list_filter = ('name', 'add_data', 'active')
    ordering = ('-id',)
    search_fields = ('name',)

class FriendTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'active', 'add_data')

admin.site.register(Post, PostAdmin)
admin.site.register(PostType, PostTypeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Friend, FriendAdmin)
admin.site.register(FriendType, FriendTypeAdmin)

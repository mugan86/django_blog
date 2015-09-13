# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Post, PostType, Category, Contact, Project, Friend, FriendType, Event, EventType, Location

#Task custom definitions
def finish_tasks(self, request, queryset):
    queryset.update(finish = True)
    #finish_tasks.short_description = u'Marcar como finalizado' 
def unfinished_tasks(self, request, queryset):
    queryset.update(finish = False)

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
    actions = [finish_tasks, unfinished_tasks]
    finish_tasks.short_description = u'Marcar como finalizado'
    unfinished_tasks.short_description = u'Marcar como no finalizado'

class FriendAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'img', 'url', 'active', 'type')
    list_filter = ('name', 'add_data', 'active')
    ordering = ('-id',)
    search_fields = ('name',)

class FriendTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'active', 'add_data')

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'type', 'url', 'logotype' ,'celebrate_data')

class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'free' ,'published_date')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'province', 'region', 'longitude' ,'latitude')

admin.site.register(Post, PostAdmin)
admin.site.register(PostType, PostTypeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Friend, FriendAdmin)
admin.site.register(FriendType, FriendTypeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventType, EventTypeAdmin)
admin.site.register(Location, LocationAdmin)

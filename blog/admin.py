# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Post, PostType, Category, Contact, Project, Friend, FriendType, Event, EventType, Location

#Add labels strings constant values
mark_to_finish = u'Finish selected projects'
mark_to_unfinish = u'No finish selected projects'

publish_selected_projects = u'Publish selected projects'
unpublish_selected_projects = u'Unpublish selected projects'

#Task custom definitions
def finish_project(self, request, queryset):
    queryset.update(finish = True)
    #finish_tasks.short_description = u'Marcar como finalizado'
def unfinished_tasks(self, request, queryset):
    queryset.update(finish = False)

def publish_action(self, request, queryset):
    queryset.update(active = True)
    #finish_tasks.short_description = u'Marcar como finalizado'
def unpublish_action(self, request, queryset):
    queryset.update(active = False)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'description', 'text', 'active' , 'category1', 'category2', 'published_date', )
    list_filter = ('author', 'published_date')
    ordering = ('-published_date',)
    search_fields = ('title',)
    actions = [publish_action, unpublish_action]
    publish_action.short_description = publish_selected_projects
    unpublish_action.short_description = unpublish_selected_projects

class PostTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'active', 'created_date','published_date', )
    list_filter = ('name', 'published_date', 'active')
    ordering = ('-published_date',)
    search_fields = ('description',)
    actions = [publish_action, unpublish_action]
    publish_action.short_description = publish_selected_projects
    unpublish_action.short_description = unpublish_selected_projects

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_date','published_date',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','received_date', )

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'start_project_date', 'active', 'finish', 'published_date')
    actions = [finish_project, unfinished_tasks]
    finish_project.short_description = mark_to_finish
    unfinished_tasks.short_description = mark_to_unfinish

class FriendAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'img', 'url', 'active', 'type')
    list_filter = ('name', 'add_data', 'active', 'type')
    ordering = ('-id',)
    search_fields = ('name',)
    actions = [publish_action, unpublish_action]
    publish_action.short_description = publish_selected_projects
    unpublish_action.short_description = unpublish_selected_projects

class FriendTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'active', 'add_data')
    actions = [publish_action, unpublish_action]
    publish_action.short_description = publish_selected_projects
    unpublish_action.short_description = unpublish_selected_projects

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'type', 'url', 'logotype' ,'celebrate_data')

class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'free' ,'published_date')
    list_filter = ('category', 'free')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'province', 'region', 'longitude' ,'latitude', 'published_date')
    list_filter = ('province', 'region')

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

# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Question
from .models import Choice


# Register your models here.
#Items to Choice model
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    list_filter = ['pub_date']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

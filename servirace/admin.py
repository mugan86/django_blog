from django.contrib import admin

# Register your models here.
from .models import Organizator
from .models import Lasterketa
from .models import Herria

# Register your models here.
#Items to Choice model
class ChoiceInline(admin.TabularInline):
    model = Lasterketa
    extra = 3

class HerriaAdmin(admin.ModelAdmin):
    list_display = ('izena', 'longitudea', 'latitudea')
    """fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    list_filter = ['pub_date']"""


class OrganizatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'tlf', 'tlf2')

class LasterketaAdmin(admin.ModelAdmin):
    list_display = ('izena', 'distantzia', 'noiz', 'start_time')

admin.site.register(Lasterketa, LasterketaAdmin)
admin.site.register(Herria, HerriaAdmin)
admin.site.register(Organizator, OrganizatorAdmin)

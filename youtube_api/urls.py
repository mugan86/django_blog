from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'youtube_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'', include('blog.urls')),
    #url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
]

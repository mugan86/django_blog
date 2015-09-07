from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.principal),
    url(r'^blog', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/category/(?P<category>[a-zA-Z]+)/$', views.post_list_by_category), ##To test...
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^event/(?P<pk>[0-9]+)/edit/$', views.event_edit, name='event_edit'),
    url(r'^about', views.about),
    url(r'^contact/', views.contact_new, name='contact_new'),
    url(r'^accounts/login/', views.login_form, name='login_form'),
    url(r'^accounts/logout/', views.logout_account, name='logout_form'),

]

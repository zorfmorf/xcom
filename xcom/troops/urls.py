from django.conf.urls import patterns, url

from troops import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<soldier_id>\d+)/$', views.soldier, name='soldier'),
)


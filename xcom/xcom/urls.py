from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xcom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
	url(r'^troops/', include('troops.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'michaela', 'michaela.views.index', name='index'),
    url(r'^$', 'troops.views.index', name='index'),
)

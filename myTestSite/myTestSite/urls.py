from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','common.views.index'),
    url(r'^polls/', include('polls.urls')),
    url(r'^jinro/', include('jinro.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

#urlpatterns += patterns('',
#    url(r'^admin/', include(admin.site.urls)),
#)

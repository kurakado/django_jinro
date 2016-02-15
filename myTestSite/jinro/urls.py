from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('jinro.views',
    url(r'^$', 'index'),
    url(r'^register/$','register'),
    url(r'^makeVillage/$','makeVillage'),
#    url(r'^(?P<poll_id>\d+)/$', 'detail'),
#    url(r'^(?P<poll_id>\d+)/results/$', 'results'),
#    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)


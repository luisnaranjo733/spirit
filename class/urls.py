from django.conf.urls import patterns, include, url

urlpatterns = patterns('class.views',
    url(r'freshmen/$', 'freshmen'),
    url(r'sophomores/$', 'sophomores'),
    url(r'juniors/$', 'juniors'),
    url(r'seniors/$', 'seniors'),
)

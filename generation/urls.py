from django.conf.urls import patterns, include, url

urlpatterns = patterns('generation.views',
    url(r'freshmen/$', 'freshmen'),
    url(r'sophomores/$', 'sophomores'),
    url(r'juniors/$', 'juniors'),
    url(r'seniors/$', 'seniors'),
)

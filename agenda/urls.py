from django.conf.urls import patterns, include, url

urlpatterns = patterns('agenda.views',
    url(r'^$', 'index', name="index"),
    url(r'^addContact/$', 'add_contact',  name='add_contact'),
    url(r'^contacto/(?P<pk>.*)/$', 'contact_detail', name='contact_detail')
)

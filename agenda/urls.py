from django.conf.urls import patterns, include, url

urlpatterns = patterns('agenda.views',
    url(r'^$', 'index', name="index"),
    url(r'^addContact/$', 'add_contact',  name='add_contact'),
    url(r'^contacto/(?P<pk>.*)/$', 'contact_detail', name='contact_detail'),
    url(r'^addGroup/$','add_group', name='add_group'),
    url(r'^Grupo/(?P<pk>.*)/$','group_detail',name='group_detail'),	
    url(r'^ShowDelGrupo/$','delete',name='delete'),
    url(r'^DelGrupo(?P<pk>.*)/$','delete_group',name='delete_group'),
    url(r'^addColor/$','add_color',name='add_color'),
    url(r'^Color/(?P<pk>.*)/$','color_detail',name='color_detail'),

)

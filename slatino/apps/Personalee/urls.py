from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('slatino.apps.Personalee.views',
    url(r'^$', 'personalee_list', name='personalee-list'),
    url(r'^(?P<personalee_id>\d+)/$', 'personalee_show'),
    url(r'^(?P<slug>\w+)/$', 'personalee_show_spec'),
)
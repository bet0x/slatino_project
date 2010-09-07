import os
from django.conf.urls.defaults import *
from settings import *
from django.shortcuts import render_to_response, get_object_or_404

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', "slatino.views.index"),
    (r'^robots\.txt$', "slatino.views.robots"),
    (r'^news/', include('slatino.News.urls')),
    (r'^article/', include('dcdjutils.Articles.urls')),
    (r'^links/', include('slatino.Links.urls')),
    (r'^personalee/', include('slatino.Personalee.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^tag/(?P<slug>\w+)/$', 'slatino.views.tag'),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),
)


if MEDIA_APACHE_DIRECT == False:
    urlpatterns += patterns('',
        (r'^(img/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(css/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(tiny_mce/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(emotions/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(news_images/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(article_images/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(personalee_images/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(articles-media/.*)$', 'django.views.static.serve', {'document_root': SITE_PATH + "dcdjutils/Articles/"}),
        (r'^tagsfield/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(LIB_PATH, "tagsfield/media/")}),
)
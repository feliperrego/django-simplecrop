from django.conf.urls import patterns, url


urlpatterns = patterns('simplecrop.views',
    url(r'^crop/$', 'crop_view'),
    url(r'^crop/upload/$', 'upload_view'),
    #url(r'^img/(?P<id>.*)/$', 'img_view'),
)
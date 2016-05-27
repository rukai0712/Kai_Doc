# encoding: utf-8

from django.conf.urls import url, patterns

urlpatterns = patterns('app1.views',
                       url(r'^app1/func/$','func', name=''),
                       )

urlpatterns += patterns('app1.views',
                       url(r'^app1/func/$','func', name=''),
                       )

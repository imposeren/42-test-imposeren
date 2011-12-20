# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
#from django.views.generic import DetailView, ListView
from testsite.mylogging.views import IndexView


urlpatterns = patterns(
    'testsite.mylogging.views',
    url(r'^$', 'index'),
)

#urlpatterns = patterns(
#    '',
#    url(r'^$',
#        ListView.as_view(queryset=Request.objects.order_by('-date')[:10])),
#)

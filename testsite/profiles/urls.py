# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
#from django.views.generic import DetailView, ListView
from testsite.profiles.views import IndexView


urlpatterns = patterns(
    'testsite.profiles.views',
    url(r'^$', 'index'),
)

#urlpatterns = patterns(
#    '',
#    url(r'^$', DetailView.as_view(model=Profile), kwargs={'pk': 1}),
#    url(r'^list/$',
#        ListView.as_view(queryset=Profile.objects.order_by('id')[:5])),
#    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Profile)),
#)
#

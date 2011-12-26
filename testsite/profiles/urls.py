# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *


urlpatterns = patterns(
    'testsite.profiles.views',
    url(r'^$', 'index', name='index'),
    url(r'^edit/$', 'edit', name='edit'),
    url(r'^tide/$', 'edit', kwargs={'reverse': 1}, name='edit-reversed'),
)

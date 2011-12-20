# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *


urlpatterns = patterns(
    'testsite.profiles.views',
    url(r'^$', 'index'),
    url(r'^edit/$', 'edit'),
)

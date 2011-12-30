# -*- coding: utf-8 -*-
"""urls go here"""
from django.conf.urls.defaults import *


urlpatterns = patterns(
    'testsite.mylogging.views',
    url(r'^$', 'index', name='index'),
    url(r'^list/$', 'listed', name='listed'),
)

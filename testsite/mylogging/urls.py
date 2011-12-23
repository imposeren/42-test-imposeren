# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *


urlpatterns = patterns(
    'testsite.mylogging.views',
    url(r'^$', 'index'),
)

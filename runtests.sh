#!/bin/sh
#nosetests --with-django --django-settings=testing.settings testing
#DJANGO_SETTINGS_MODULE=testing.settings NOSE_WITH_DJANGO=1 nosetests testing
DJANGO_SETTINGS_MODULE=testsite.settings ./django-nosetests.py testsite

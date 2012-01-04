# -*- coding: utf-8 -*-
from tddspry.django import HttpTestCase
from tddspry.django import TestCase
from django.core.handlers.wsgi import WSGIRequest


myfixtures = ['profiles/fixtures/post_migrate.json',
              'mylogging/fixtures/post_migrate.json',
              'auth.json',
              ]


class MyHttpTestCase(HttpTestCase):
    fixtures = myfixtures


class MyTestCase(TestCase):
    fixtures = myfixtures
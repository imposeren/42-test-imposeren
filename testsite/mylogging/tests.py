# -*- coding: utf-8 -*-
from tddspry.django import HttpTestCase
from tddspry.django import TestCase
from testsite.mylogging.models import Request
from testsite.mylogging.templatetags.mylogging_tags import edit_link
from django.test.client import RequestFactory
from django.template import RequestContext
from django.template import Template
from django import template


class TestLogger(HttpTestCase):
    def test_counts(self):
        self.go200('/')
        count_cur = len(Request.objects.all())
        self.go200('/')
        self.assert_count(Request, (count_cur + 1))

        count_cur = len(Request.objects.all())
        self.go200('/requests/')
        self.assert_count(Request, (count_cur + 1))
        self.go200('/requests/')
        self.find(r"\bGET(\s)+/requests/ ")
        self.find(r"\bGET(\s)+/")


class testTag(TestCase):
#    def setUp(self):
#        register = template.Library()
#        template.libraries['django.templatetags.mylogging_tags'] = register
#        register.tag('edit_link ', edit_link)

    def test_tag(self):
        factory = RequestFactory()
        request = factory.get('/')
        context = RequestContext(request, {'foo': 'bar'})
        out = Template(
            "{% load mylogging_tags %}"
            "{% edit_link request.user %}"
        ).render(context)
        self.asserEquals(rendered, "/admin/auth/user/1/")
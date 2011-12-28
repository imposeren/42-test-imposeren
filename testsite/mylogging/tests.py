# -*- coding: utf-8 -*-
from tddspry.django import HttpTestCase
from tddspry.django import TestCase
from testsite.mylogging.models import Request
from django.test import Client
from django.core.handlers.wsgi import WSGIRequest
from django.template import RequestContext
from django.template import Template
from django.contrib.auth.models import User


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


## http://djangosnippets.org/snippets/963/
class RequestFactory(Client):
    """
    Class that lets you create mock Request objects for use in testing.

    Usage:

    rf = RequestFactory()
    get_request = rf.get('/hello/')
    post_request = rf.post('/submit/', {'foo': 'bar'})

    This class re-uses the django.test.client.Client interface, docs here:
    http://www.djangoproject.com/documentation/testing/#the-test-client

    Once you have a request object you can pass it to any view function,
    just as if that view had been hooked up using a URLconf.

    """

    def request(self, **request):
        """
        Similar to parent class, but returns the request object as soon as it
        has created it.
        """
        environ = {
            'HTTP_COOKIE': self.cookies,
            'PATH_INFO': '/',
            'QUERY_STRING': '',
            'REQUEST_METHOD': 'GET',
            'SCRIPT_NAME': '',
            'SERVER_NAME': 'testserver',
            'SERVER_PORT': 80,
            'SERVER_PROTOCOL': 'HTTP/1.1',
        }
        environ.update(self.defaults)
        environ.update(request)
        return WSGIRequest(environ)
## end of http://djangosnippets.org/snippets/963/


class testTag(TestCase):
#    def setUp(self):
#        register = template.Library()
#        template.libraries['django.templatetags.mylogging_tags'] = register
#        register.tag('edit_link ', edit_link)

    def test_tag(self):
        factory = RequestFactory()
        factory.login(username='admin', password='admin')
        request = factory.get('/')
        request.user = User.objects.get(username='admin')
        context = RequestContext(request)
        out = Template(
            "{% load mylogging_tags %}"
            "{% edit_link user %}"
        ).render(context)
        self.assertEquals(out, "/admin/auth/user/1/")
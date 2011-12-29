# -*- coding: utf-8 -*-
from testsite.mylogging.models import Request
from testsite.extra_common.testcases import (MyHttpTestCase, MyTestCase,
                                             RequestFactory)
from django.template import RequestContext
from django.template import Template


class TestLogger(MyHttpTestCase):
    def test_counts(self):
        self.go200('/')
        count_cur = Request.objects.count()
        self.go200('/')
        self.assert_count(Request, (count_cur + 1))

        count_cur = Request.objects.count()
        self.go200('/requests/')
        self.assert_count(Request, (count_cur + 1))
        self.go200('/requests/')
        self.find(r"\bGET(\s)+/requests/ ")
        self.find(r"\bGET(\s)+/")


class testTag(MyTestCase):
#    def setUp(self):
#        register = template.Library()
#        template.libraries['django.templatetags.mylogging_tags'] = register
#        register.tag('edit_link ', edit_link)

    def test_tag(self):
        from django.contrib.auth.models import User
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

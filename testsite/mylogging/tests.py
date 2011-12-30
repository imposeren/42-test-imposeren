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

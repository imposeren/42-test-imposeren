# -*- coding: utf-8 -*-
from testsite.extra_common.testcases import MyTestCase, RequestFactory
from django.template import RequestContext
from testsite.extra_common.context_processors import add_settings
from django.conf import settings
from django.core import management


class TestContext(MyTestCase):

    def test_it(self):
        factory = RequestFactory()
        request = factory.get('/')
        context = RequestContext(request, {'foo': 'bar'}, [add_settings])
        self.assertIn('settings', context)
        self.assertEqual(context['settings'], settings)

class testManagement(MyTestCase):
    def test_modelstats(self):
        result = management.call_command('modelstats', verbosity=0,
                                         interactive=False)

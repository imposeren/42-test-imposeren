# -*- coding: utf-8 -*-
from testsite.extra_common.testcases import MyTestCase, RequestFactory
from testsite.extra_common.management.commands.modelstats import modelstats
from django.template import RequestContext
from testsite.extra_common.context_processors import add_settings
from django.conf import settings
from django.core import management
from testsite.profiles.models import Profile
from testsite.mylogging.models import Request
import datetime


class TestContext(MyTestCase):

    def test_it(self):
        factory = RequestFactory()
        request = factory.get('/')
        context = RequestContext(request, {'foo': 'bar'}, [add_settings])
        self.assertIn('settings', context)
        self.assertEqual(context['settings'], settings)

class testManagement(MyTestCase):
    def test_modelstats(self):
        PROFILE = 'testsite.profiles.models.Profile'
        REQUEST = 'testsite.mylogging.models.Request'
        management.call_command('modelstats', verbosity=0,
                                interactive=False)
        # just test if this does not raise anything

        result = modelstats()
        self.assertIn(PROFILE, result)
        self.assertIn(REQUEST, result)
        profiles_num_0 = int(result[result.find(PROFILE):].split()[1])
        requests_num_0 = int(result[result.find(REQUEST):].split()[1])
        Profile(name="TestName",
                surname="TestSur",
                bio='no bio',
                birth=datetime.datetime(1987, 12, 11, 0, 0)).save()
        Profile(name="TestName2",
                surname="TestSur",
                bio='no bio',
                birth=datetime.datetime(1987, 12, 11, 0, 0)).save()
        self.go('/')
        self.go('/')
        self.go('/')
        result = modelstats()
        profiles_num_1 = int(result[result.find(PROFILE):].split()[1])
        requests_num_1 = int(result[result.find(REQUEST):].split()[1])
        self.assertEqual(profiles_num_0 + 2, profiles_num_1)
        self.assertEqual(requests_num_0 + 3, requests_num_1)




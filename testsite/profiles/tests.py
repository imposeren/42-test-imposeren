# -*- coding: utf-8 -*-
"""Tests go here"""
from django.conf import settings
from tddspry.django import HttpTestCase
from tddspry.django import TestCase
from testsite.profiles.models import Profile
from django.test.client import RequestFactory
from django.template import RequestContext
from testsite.context_processors import add_settings
import datetime


class TestProfileModel(TestCase):
    """Test if Profile can be created and contacts associated

    """
    fixtures = ['testsite/initial_data.json']

    def test_add(self):
        self.assert_create(Profile,
                           name="TestName",
                           surname="TestSur",
                           bio='no bio',
                           birth=datetime.datetime(1987, 12, 11, 0, 0)
                           )

        user2 = Profile(name="TestName2",
                        surname="TestSur2",
                        bio='no bio2',
                        birth=datetime.datetime(1987, 12, 11, 0, 0))
        user2.save()
        self.assert_true(user2.contact_set.create(mean='phone',
                                                  data='+38(044)999-99-99'))


class TestProfile(HttpTestCase):
    def test_content(self):
        self.go200('/')
        self.find("Bio")
        self.find("Contacts")
        self.find("Photo")
        self.find("Date of Birth")
        self.find("mail")
        self.find("phone")


class TestContext(TestCase):

    def test_it(self):
        factory = RequestFactory()
        request = factory.get('/')
        context = RequestContext(request, {'foo': 'bar'}, [add_settings])
        self.assertIn('settings', context)
        self.assertEqual(context['settings'], settings)


class TestForms(HttpTestCase):
    def test_auth_links(self):
        login_url = self.build_url('django.contrib.auth.views.login')
        logout_url = self.build_url('django.contrib.auth.views.logout')
        edit_url = self.build_url('profiles:edit')
        self.go200('/')

        self.notfind(logout_url)
        self.find(edit_url)
        self.notfind(login_url)

        self.go200(edit_url)
        self.find(login_url)
        self.login('admin', 'admin')

        self.go200(edit_url)
        self.find(logout_url)
        self.notfind(login_url)
        self.logout()

    def test_edit(self):
        self.login('admin', 'admin')
        edit_url = self.build_url('profiles:edit')
        view_url = self.build_url('profiles:index')
        self.go200(edit_url)
        self.formvalue(1, "name", "Value")
        self.formvalue(1, "surname", "Value")
        self.formvalue(1, "bio", "Value")
        self.formvalue(1, "birth", "2010-12-12")
        self.formvalue(1, "contact_set-0-data", "m@m.com")  # email
        self.formvalue(1, "contact_set-1-data", "+800 555 55 55")  # phone
        self.find("Photo")

        #self.submit200(11, url=view_url)
        self.submit200()
        self.go200(view_url)
        self.find(r"Name.*: Value")
        self.find(r"Last name.*: Value")
        self.find(r"Bio.*:.*Value")
        self.find(r"Date of Birth.*:\s+Dec. 12, 2010")
        self.find(r"m@m.com")
        self.find(r"800 555 55 55")

        #test wrong form
        self.go200(edit_url)
        self.formvalue(1, "birth", "ababab")
        self.submit200()  # back on edit page
        self.find('Errors')
        self.find('Enter a valid date')

#        #test unauthorized edit
#        self.logout()
#        self.go(edit_url)
#        self.formvalue(1, "name", "Value2")
#        self.submit200()  # back on edit page
#        self.find('not authorized')


import os
from windmill.authoring import djangotest


class TestProjectWindmillTest(djangotest.WindmillDjangoUnitTest):
    test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            'windmilltests')
    browser = 'firefox'


class TestReversedForm(HttpTestCase):
    def test(self):
        edit_url = self.build_url('profiles:edit')
        self.go200(edit_url)
        self.login('admin', 'admin')
        self.find('Reverse')
        self.go200(self.build_url('profiles:edit-reversed'))
        self.find('Photo.*Date of Birth.*Last Name.*Name.*')
#from django.conf import settings
from django.conf import settings
from tddspry.django import HttpTestCase
#from tddspry.django import DatabaseTestCase
from tddspry.django import TestCase
from testsite.profiles.models import Profile#, Contact
from testsite.mylogging.models import Request
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
                           birth=datetime.datetime(1987, 12, 11, 0,0)
                           )

        user2 = Profile(name="TestName2",
                        surname="TestSur2",
                        bio='no bio2',
                        birth=datetime.datetime(1987, 12, 11, 0,0))
        user2.save()
        self.assert_true(user2.contact_set.create(mean='phone',
                                                  data='+38(044)999-99-99'))

class TestProfile(HttpTestCase):
    def test_content(self):
        self.go200('/')
        self.find("Bio")
        self.find("Contacts")
        self.find("mail")
        self.find("phone")


class TestLogger(HttpTestCase):
    def test_counts(self):
        self.go200('/')
        count_cur = len(Request.objects.all())
        self.go200('/')
        self.assert_count(Request, (count_cur + 1))
                
        count_cur = len(Request.objects.all())
        self.go200('/requests/')
        self.assert_count(Request, (count_cur + 1))
        self.find(r"\bGET(\s)+/requests/ ")
        self.find(r"\bGET(\s)+/")
        
from django.test.client import RequestFactory 
from django.template import RequestContext
from context_processors import add_settings
class TestContext(TestCase):
    def test_it(self):
        factory = RequestFactory()
        request = factory.get('/')
        context = RequestContext(request, {'foo': 'bar'}, [add_settings])
        self.assertIn('settings', context)
        self.assertEqual(context['settings'], settings)
        
class TestForms(TestCase):
    def test_index_links(self):
        login_url = self.build_url('django.contrib.auth.views.login')
        logout_url = self.build_url('django.contrib.auth.views.logout')
        edit_url = self.build_url('testsite.profiles.edit')
        self.go200('/')
        
        
        self.notfind(logout_url)
        self.notfind(edit_url)
        self.find(login_url)
        
        self.login('admin', 'admin')
        self.find(logout_url)
        self.find(edit_url)
        self.notfind(login_url)
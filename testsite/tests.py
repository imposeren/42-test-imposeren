#from django.conf import settings
import settings
from tddspry.django import HttpTestCase
#from tddspry.django import DatabaseTestCase
from tddspry.django import TestCase
from testsite.profiles.models import Profile#, Contact
from testsite.mylogging.models import Request

class TestProfileModel(TestCase):
    """Test if Profile can be created and contacts associated
    
    """
    fixtures = ['testsite/initial_data.json']
    def test_add(self):
        self.assert_create(Profile,
                           name="TestName",
                           surname="TestSur",
                           bio='no bio')

        user2 = Profile(name="TestName2",
                            surname="TestSur2",
                            bio='no bio2')
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
        self.find(r"\bGET /\b")
                
        count_cur = len(Request.objects.all())
        self.go200('/requests/')
        self.assert_count(Request, (count_cur + 1))
        self.find(r"\bGET /requests/\b")
        
        

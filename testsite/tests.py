#from django.conf import settings
import settings
from tddspry.django import HttpTestCase
from tddspry.django import TestCase
from testsite.profiles.models import Profile, Contact

class TestUserModel(TestCase):
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


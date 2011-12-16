from tddspry.django import HttpTestCase

#from django.conf import settings


class TestProfile(HttpTestCase):
    fixtures = ['initial_data.json']
    def test_content(self):
        self.go200('/')
        self.find("Bio")
        self.find("Contacts")
        self.find("mail")
        self.find("phone")


from profiles import Profile, Contact

class TestUserModel(TestCase):
    def test_add(self):
        self.assert_create(Profile,
                           name="TestName",
                           surname="TestSur",
                           bio='no bio')

        user2 = Profile(name="TestName2",
                            surname="TestSur2",
                            bio='no bio2')
        self.assert_true(user2.contact_set.create(mean='phone',
                                                  data='+38(044)999-99-99'))

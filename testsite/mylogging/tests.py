# -*- coding: utf-8 -*-
from testsite.mylogging.models import Request, Modellog
from testsite.profiles.models import Profile
from testsite.extra_common.testcases import MyHttpTestCase, MyTestCase
import datetime


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


class testDBLogging(MyTestCase):
    def test_it(self):
        logs_count = Modellog.objects.count()

        #test creation log
        prof = Profile(name="TestName",
                       surname="TestSur",
                       bio='no bio',
                       birth=datetime.datetime(1987, 12, 11, 0, 0)
                       )
        prof.save()
        latest = Modellog.objects.latest()
        self.assertEqual(logs_count + 1, Modellog.objects.count())
        self.assertEqual(latest.action, 'create')
        self.assertEqual(latest.inst_pk, prof.pk)
        self.assertEqual(latest.app, prof._meta.app_label)
        self.assertEqual(latest.model, prof._meta.object_name)

        #test modification log
        prof.name = "NewName"
        prof.save()
        self.assertEqual(logs_count + 2, Modellog.objects.count())
        self.assertEqual(Modellog.objects.latest().action, 'edit')

        #test deletion log
        prof.delete()
        self.assertEqual(Modellog.objects.latest().action, 'delete')
        self.assertEqual(logs_count + 3, Modellog.objects.count())

        #test another creation log
        self.go('/')  # let pk be greater than 1
        req = Request(method='GET', path='/', get='', post='')
        req.save()
        self.assertEqual(logs_count + 5, Modellog.objects.count())
        latest = Modellog.objects.latest()
        self.assertEqual(latest.inst_pk, req.pk)
        self.assertEqual(latest.app, req._meta.app_label)
        self.assertEqual(latest.model, req._meta.object_name)

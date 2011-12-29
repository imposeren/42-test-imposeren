# -*- coding: utf-8 -*-
import os
from windmill.authoring import djangotest
from testsite.extra_common.testcases import myfixtures


class javascript_wm_Tests(djangotest.WindmillDjangoUnitTest):
    fixtures = myfixtures
    test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            'windmilltests')
    browser = 'firefox'

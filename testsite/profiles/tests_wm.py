# -*- coding: utf-8 -*-
import os
from windmill.authoring import djangotest


class javascript_wm_Tests(djangotest.WindmillDjangoUnitTest):
    test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            'windmilltests')
    browser = 'firefox'

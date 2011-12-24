# -*- coding: utf-8 -*-
from testsite.mylogging.models import Request


class LogRequest(object):
    """Log every http request to database"""
    def process_request(self, request):
        req = Request(method=request.method, path=request.path,
                      get=request.GET, post=request.POST)
        req.save()
        return None

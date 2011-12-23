# -*- coding: utf-8 -*-
from testsite.mylogging.models import Request


class LogRequest(object):
    def process_request(self, request):
        r = Request(method=request.method, path=request.path, get=request.GET,
                post=request.POST)
        r.save()
        return None

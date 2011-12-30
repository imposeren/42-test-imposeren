"""views go here"""
from django.views.generic import ListView
from testsite.mylogging.models import Request
from django.core.paginator import (Paginator, InvalidPage, EmptyPage)
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson


class IndexView(ListView):
    """Show first 10 http requests """
    queryset = Request.objects.order_by('date')[:10]


def index(request):
    return IndexView.as_view()(request)


def listed(request, sortby='date'):
    template = 'mylogging/request_sorted.html'
    if (request.method == 'POST' and request.user.is_authenticated()
    and request.is_ajax()):
        request_id = int(request.POST['request_id'])
        new_value = int(request.POST['value'])
        try:
            req = Request.objects.get(pk=request_id)
            req.priority = new_value
            req.save()
        except Exception:
            return HttpResponse(simplejson.dumps({'result': 'error'}),
                                mimetype='application/javascript')
        return HttpResponse(simplejson.dumps({'result': 'success',
                                              'value': req.priority}),
                            mimetype='application/javascript')
    else:
        if sortby.endswith('date'):
            sortby = [sortby, 'priority']
        elif sortby.endswith('priority'):
            sortby = [sortby, 'date']
        else:
            sortby = ['date', 'priority']

        request_list = Request.objects.all().order_by(*sortby)
        paginator = Paginator(request_list, 10)
        page = request.GET.get('page')
        try:
            requests = paginator.page(page)
        except TypeError:
            requests = paginator.page(1)
        except (EmptyPage, InvalidPage):
            requests = paginator.page(paginator.num_pages)
        return render_to_response(template, {'requests': requests,
                                             'sortby': sortby[0]},
                                  context_instance=RequestContext(request))

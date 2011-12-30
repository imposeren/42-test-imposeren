"""views go here"""
from django.views.generic import ListView
from testsite.mylogging.models import Request
from django.core.paginator import (Paginator, InvalidPage, EmptyPage)
from django.shortcuts import render_to_response
from django.template import RequestContext


class IndexView(ListView):
    """Show first 10 http requests """
    queryset = Request.objects.order_by('date')[:10]


def index(request):
    return IndexView.as_view()(request)


def listed(request, sortby='date'):
    template = 'mylogging/request_sorted.html'
    if (request.method == 'POST' and request.user.is_authenticated()
    and request.is_ajax()):
        pass
          # do something with it and update
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
        return render_to_response(template, {'requests': requests},
                                  context_instance=RequestContext(request))

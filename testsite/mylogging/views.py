"""views go here"""
from django.views.generic import ListView
from testsite.mylogging.models import Request


class IndexView(ListView):
    """Show first 10 http requests """
    queryset = Request.objects.order_by('date')[:10]


def index(request):
    return IndexView.as_view()(request)

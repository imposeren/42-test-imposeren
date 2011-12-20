"""views go here"""
from django.views.generic import ListView
from testsite.mylogging.models import Request

from testsite.decorators import superuser_only

class IndexView(ListView):
    queryset = Request.objects.order_by('-date')[:10]

@superuser_only
def index(request):
    return IndexView.as_view()(request)

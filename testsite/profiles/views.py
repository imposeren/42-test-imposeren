from django.views.generic import DetailView
from testsite.profiles.models import Profile


class IndexView(DetailView):
    """Details on profile"""
    model = Profile


def index(request):
    """Show detail on me"""
    return IndexView.as_view()(request, pk=1)
    
def edit(request, pk=1):
    return IndexView.as_view()(request, pk=1)
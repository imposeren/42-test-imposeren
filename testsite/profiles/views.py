from django.views.generic import DetailView
from testsite.profiles.models import Profile


class IndexView(DetailView):
    model = Profile


def index(request):
    return IndexView.as_view()(request, pk=1)

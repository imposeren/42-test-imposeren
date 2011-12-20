from django.views.generic import DetailView
from testsite.profiles.models import Profile


class IndexView(DetailView):
    """Details on profile"""
    model = Profile


def index(request):
    """Show detail on me"""
    return IndexView.as_view()(request, pk=1)
    
from django.forms.models import modelformset_factory
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from testsite.decorators import superuser_only

@superuser_only
def edit(request, pk=1):
    ProfileFormSet = modelformset_factory(Profile, max_num=1)

    if request.method == 'POST':
        formset = ProfileFormSet(request.POST, request.FILES,
                                 queryset=Profile.objects.filter(pk=1))
        if formset.is_valid():
            formset.save()
        return redirect(index)
    else:
        formset = ProfileFormSet(queryset=Profile.objects.filter(pk=1))

    return render_to_response('profiles/edit.html', {'formset':formset},
                              context_instance = RequestContext(request))
 
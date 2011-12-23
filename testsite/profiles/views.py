from django.views.generic import DetailView
from testsite.profiles.models import Profile
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from testsite.profiles.forms import ContactFormSet, ProfileForm, readonly


class IndexView(DetailView):
    """Details on profile"""
    model = Profile


def index(request):
    """Show detail on me"""
    return IndexView.as_view()(request, pk=1)


def edit(request, pk=1, errors=None):
    if errors is None:
        errors = []
    target = Profile.objects.get(pk=pk)

    if request.method == 'POST' and request.user.is_authenticated():
        profile = ProfileForm(request.POST, request.FILES, instance=target)
        contacts = ContactFormSet(request.POST, request.FILES,
                                   instance=target)
        if profile.is_valid() and contacts.is_valid():
            contacts.save()
            profile.save()
            return redirect(index)
        else:
            if not profile.is_valid():
                errors.append(profile.errors)
            if not contacts.is_valid():
                errors.append(contacts.errors)
    if not request.user.is_authenticated():
        errors.append('You are not authorized to edit this form')
    if (request.method == 'GET' or len(errors) or
    not request.user.is_authenticated()):
        profile = ProfileForm(instance=target)
        contacts = ContactFormSet(instance=target)
        if not request.user.is_authenticated():
            readonly(profile)
            readonly(contacts)

    return render_to_response('profiles/edit.html', {'profile': profile,
                                                     'contacts': contacts,
                                                     'errors': errors},
                              context_instance=RequestContext(request))

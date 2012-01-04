# -*- coding: utf-8 -*-
"""Views go here"""
from django.views.generic import DetailView
from testsite.profiles.models import Profile
from django.template import RequestContext
from django.shortcuts import render_to_response
from testsite.profiles.forms import ContactFormSet, ProfileForm, readonly
from django.http import HttpResponse
from django.utils import simplejson
from django.forms.util import ErrorDict


class IndexView(DetailView):
    """Details on profile"""
    model = Profile


def index(request):
    """Show detail on me"""
    return IndexView.as_view()(request, pk=1)


def edit(request, pk=1, errors=None, reverse=False):
    """Edit main profile data if user is authorized"""
    template = 'profiles/edit.html'
    result = 'Error'
    if errors is None:
        errors = ErrorDict()
    target = Profile.objects.get(pk=pk)
    if request.method == 'POST' and request.user.is_authenticated():
        profile = ProfileForm(request.POST, request.FILES, instance=target)
        contacts = ContactFormSet(request.POST, request.FILES,
                                   instance=target)
        if profile.is_valid() and contacts.is_valid():
            contacts.save()
            profile.save()
            result = 'Done'
        if not profile.is_valid():
            errors.update(profile.errors)
        if not contacts.is_valid():
            for num, suberrors in enumerate(contacts.errors):
                if suberrors:
                    for field, error in suberrors.iteritems():
                        field_id = "%s-%s-%s" % (contacts.prefix, num, field)
                        errors.update({field_id: error})
    if (request.method == 'GET' or not request.user.is_authenticated()
      or errors):
        profile = ProfileForm(instance=target)
        contacts = ContactFormSet(instance=target)
        if reverse:
            profile.fields.keyOrder.reverse()
            contacts.forms.reverse()
            template = 'profiles/edit_reversed.html'
        if not request.user.is_authenticated():
            readonly(profile)
            readonly(contacts)
            errors['auth: '] = 'you are not authorized to edit this form'

    if request.is_ajax():
        return HttpResponse(simplejson.dumps({'result': result,
                                              'errors': errors}),
                            mimetype='application/javascript')
    else:
        print(errors)
        return render_to_response(template, {'profile': profile,
                                             'contacts': contacts,
                                             'errors': errors},
                                  context_instance=RequestContext(request))

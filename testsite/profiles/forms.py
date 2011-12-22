# -*- coding: utf-8 -*-
from django.forms import ModelForm
from testsite.profiles.models import Contact, Profile
from django.forms.models import inlineformset_factory
from django.forms.models import BaseModelFormSet


def readonly(form_or_set):
    """Make form or formset readonly"""
    if isinstance(form_or_set, ModelForm):
        for field in form_or_set.fields.keys():
            form_or_set.fields[field].widget.attrs['readonly'] = True
    elif isinstance(form_or_set, BaseModelFormSet):
        for form in form_or_set:
            readonly(form)


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )


class ContactForm(ModelForm):
    class Meta:
        model = Contact


ContactFormSet = inlineformset_factory(Profile, Contact, max_num=5)
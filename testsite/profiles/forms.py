# -*- coding: utf-8 -*-
"""Forms go here"""
from django import forms
from testsite.profiles.models import Contact, Profile
from django.forms.models import inlineformset_factory
from django.forms.models import BaseModelFormSet


def readonly(form_or_set):
    """Make form or formset readonly"""
    if isinstance(form_or_set, forms.ModelForm):
        for field in form_or_set.fields.keys():
            form_or_set.fields[field].widget.attrs['readonly'] = True
    elif isinstance(form_or_set, BaseModelFormSet):
        for form in form_or_set:
            readonly(form)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )
        widgets = {
            'bio': forms.Textarea(attrs={'cols': '20', 'rows': '10'})
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'mean': forms.TextInput(attrs={'size': '10'}),
            'data': forms.TextInput(attrs={'size': '21'}),
        }


ContactFormSet = inlineformset_factory(Profile, Contact, max_num=5, form=ContactForm)

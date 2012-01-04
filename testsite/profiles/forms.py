# -*- coding: utf-8 -*-
from django import forms
from testsite.profiles.models import Contact, Profile
from django.forms.models import inlineformset_factory
from django.forms.models import BaseModelFormSet
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re


def readonly(form_or_set):
    """Make form or formset readonly"""
    if isinstance(form_or_set, forms.ModelForm):
        for field in form_or_set.fields.keys():
            form_or_set.fields[field].widget.attrs['disabled'] = True
    elif isinstance(form_or_set, BaseModelFormSet):
        for form in form_or_set:
            readonly(form)


class CalendarWidget(forms.TextInput):
    class Media:
        css = {
            'all': ('css/jquery-ui.css',)
        }
        js = ('js/select_birth.js',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )
        widgets = {
            'bio': forms.Textarea(attrs={'cols': '20', 'rows': '10'}),
            'birth': CalendarWidget(),
        }


PHONE_REGEXP = r"^(\+|0)?([0-9]{3})?[0-9]{9}$"


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'mean': forms.TextInput(attrs={'size': '10'}),
            'data': forms.TextInput(attrs={'size': '21'}),
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        mean = cleaned_data.get("mean")
        data = cleaned_data.get("data")

        if re.match('e?mail', mean):
            try:
                cleaned_data["mean"] = "email"
                validate_email(data)
            except ValidationError, msgs:
                message = "Enter a valid e-mail address."
                self._errors["data"] = self.error_class([message])
                del cleaned_data["data"]

        elif re.match('phone.*', mean):
            for ignoreit in [' ', '(', ')']:
                data = data.replace(ignoreit, '')
            if not re.match(PHONE_REGEXP, data):
                message = "Enter a valid phone number."
                self._errors["data"] = self.error_class([message])
                del cleaned_data["data"]
            else:
                cleaned_data["data"] = data

        return cleaned_data


ContactFormSet = inlineformset_factory(Profile, Contact,
                                       form=ContactForm)

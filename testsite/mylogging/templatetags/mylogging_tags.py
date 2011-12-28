# -*- coding: utf-8 -*-
"""tags go here"""
from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def edit_link(context, obj):
    #obj = context[objname]
    #obj = template.Variable(objname)
    url = reverse('admin:%s_%s_change' % (obj._meta.app_label,
                                          obj._meta.module_name),
                  args=[obj.id])
    return url

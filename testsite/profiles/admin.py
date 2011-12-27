# -*- coding: utf-8 -*-
from testsite.profiles.models import Profile, Contact
from django.contrib import admin


admin.site.register(Contact)


class ContactInline(admin.StackedInline):
    model = Contact
    extra = 2


class ProfileAdmin(admin.ModelAdmin):
    inlines = [ContactInline]


admin.site.register(Profile, ProfileAdmin)

from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import DetailView
from profiles.models import Profile


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', DetailView.as_view(model=Profile), kwargs={'pk': 1}),
    url(r'^profile/', include('testsite.profiles.urls')),
    url(r'^requests/', include('testsite.mylogging.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

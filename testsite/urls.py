from django.conf.urls.defaults import patterns, include, url
from staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import DetailView
from profiles.models import Profile
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', DetailView.as_view(model=Profile), kwargs={'pk': 1}),
    url(r'^profile/', include('testsite.profiles.urls',
                              app_name='profiles',
                              namespace='profiles')),
    url(r'^requests/', include('testsite.mylogging.urls',
                               app_name='mylogging',
                               namespace='mylogging')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        kwargs={'next_page': '/'}),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^call/', include('askq.urls', namespace="askq")),
    url(r'^admin/', include(admin.site.urls)),
)

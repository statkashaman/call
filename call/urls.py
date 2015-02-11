from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from call import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^call/', include('askq.urls', namespace="askq")),
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

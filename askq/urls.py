from django.conf.urls import patterns, url
from askq import views


urlpatterns = patterns('',
   #url(r'^$', views.Projects.as_view(),name='index'),
   url(r'^(?P<pk>\d+)/$', views.Asks.as_view(), name='detail'),
   url(r'^$',views.index),
)

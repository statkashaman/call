from django.conf.urls import patterns, url
from askq import views


urlpatterns = patterns('',
   #url(r'^$', views.Projects.as_view(),name='index'),
   url(r'^$',views.index),
)

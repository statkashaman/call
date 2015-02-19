from django.conf.urls import patterns, url
from askq import views

urlpatterns = patterns('',
   url(r'^$',views.index,name='index'),
   url(r'^stat/',views.statistics,name='statistics'),
   url(r'^excel_output/',views.excel_output,name='Excel'),
)

from django.conf.urls.defaults import *
from Ujima.mapping.views import *

urlpatterns = patterns('',
                         
                         (r'data/(?P<app>[-a-z]+)/(?P<country>[-a-z]+)/', country_data),
                       
)


from django.conf.urls.defaults import *
from usaid.aid.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                      (r'country/$', country_list),
                      (r'vendor/$', vendor_list),
                      (r'search/$', search_detail),
                      (r'product/$', prod_list),
                      (r'country/(?P<country>[-a-z]+)/$', country_detail),
                      (r'product/(?P<prodcode>[-a-z]+)/$', prod_detail),
                      (r'vendor/(?P<vendors>[-a-z]+)/$', vendor_detail),
                      (r'country/(?P<country>[-a-z]+)/(?P<year>\d+)/$',country_year),
    # Example:
    # (r'^usaid/', include('usaid.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)

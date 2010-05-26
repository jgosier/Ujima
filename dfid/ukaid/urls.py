from django.conf.urls.defaults import *
from dfid.ukaid.views import *

# Uncomment the next two lines to enable the admin:


urlpatterns = patterns('',
                      (r'country/$', country_list),
                      (r'projects/$', project_list),
                      (r'search/$', search_detail),
                      (r'risk/$', risk_list),
                      (r'type/$', type_list), 
                      (r'country/(?P<country>[-a-z]+)/$', country_detail),
                      (r'projects/(?P<projects>[-\w]+)/$', project_detail),
                      (r'risk/(?P<risk>[-a-z]+)/$', risk_detail),
                      (r'country/(?P<country>[-a-z]+)/(?P<year>\d+)/$',country_year),
    # Example:
    # (r'^dfid/', include('dfid.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/(.*)', admin.site.root),
)

from django.conf.urls.defaults import *
from weapons.arms.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                      (r'country/$', country_list),
                      (r'weapon/$', weapons_list),
                      (r'country/(?P<country>[-a-z]+)/$', country_detail),
                      (r'weapon/(?P<weapon>[-a-z]+)/$', weapon_detail),
    # Example:
    # (r'^weapons/', include('weapons.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
)

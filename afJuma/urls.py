from django.conf.urls.defaults import *
from Ujima.afJuma.afdb.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                      (r'bcountry/$', bcountry_list),
                      (r'bidder/$', bidder_list),
                      (r'pcountry/$', pcountry_list),
                      (r'expense/$', expense_list),
                      (r'procure/$', proc_list),
                       
                       
                      (r'search/$', search_detail),
                      (r'projcountry/(?P<pcountry>[-a-z]+)/$', pcountry_detail),
                      (r'bidcountry/(?P<bcountry>[-a-z]+)/$', bcountry_detail),
                      (r'expensecategory/(?P<expense>[-a-z]+)/$', expense_detail),
                      (r'bidder/(?P<bidder>[-a-z]+)/$', bidder_detail),
                      (r'procuremode/(?P<mode>[-a-z]+)/$',procuremode),
                       (r'projcountry/(?P<pcountry>[-a-z]+)/(?P<year>\d+)/$', pcountry_year),
                       (r'bidder/(?P<bidder>[-a-z]+)/(?P<year>\d+)/$', bidder_year),
                       (r'flag/(?P<country>[-\w]+)/',country_flag),
    # Example:
    # (r'^usaid/', include('usaid.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)

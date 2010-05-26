from django.conf.urls.defaults import *

from globalfund.views import *
from Ujima.main.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from Ujima.settings import MEDIA_ROOT
from Ujima.docshare.views import *
from Ujima.weapons.arms.views import country_flag
from Ujima.mapping.views import marker,kml_file,draw_map,country_page




###lobying urls



urlpatterns=patterns('',
                         #(r'^charts/simple.png$', simple),
                                                  (r'^faq$', faq,{'template':'main/faq.html'}),
                                                  (r'^contact', contact,{'template':'main/contact.html'}),
						 
						(r'^(?P<app>\w+)/(?P<model>[-\w]+)/csv/$', export),
                         (r'^(?P<app>\w+)/(?P<model>\w+)/(?P<slug>[-\w]+)/csv/$', export2),
                        (r'^docs/$',Document_list,{'template':'main/document.html'}),
                        (r'^about/$',about,{'template':'main/about.html'}),
                        (r'^docs/(?P<doc_id>[1234567890]+)/$',document_viewer,{'template':'main/docs.html'}),
			(r'^$',index,{'template':'base.html'}),
                       (r'^globalfund/country/$', country_list),
                      (r'^globalfund/region/$', region_list),
                      (r'^globalfund/orgtype/$', orgtype_list),
                      (r'^globalfund/disease/$', disease_list),
                      (r'^mapping/$', draw_map),
                       (r'^xd_receiver.htm',faq,{'template':'xd_receiver.htm'}),
                        (r'^googlehostedservice.html',faq,{'template':'googlehostedservice.html'}),
                       (r'^comments/', include('django.contrib.comments.urls')), 
                      (r'^globalfund/country/(?P<country>[-a-z]+)/$', country_detail),
                      (r'^globalfund/region/(?P<region>[-a-z]+)/$', region_detail),
                      (r'^globalfund/disease/(?P<disease>[-a-z]+)/$', disease_detail),
                      (r'^globalfund/orgtype/(?P<orgtype>[-a-z]+)/$', orgtype_detail),
                      (r'^globalfund/orgsearch/$', orgsearch_detail),
                      (r'search/$',google_search),
                      
                       (r'^lobby/', include('lobby.urls')),
                        (r'^afdb/', include('afJuma.urls')),
                        (r'^marker/(?P<radius>[\d]+)/(?P<color>[-a-z]+)/(?P<opacity>[\d]+)/', marker),
                        (r'^marker/(?P<radius>[\d]+)/(?P<color>[-a-z]+)/', marker),
                        (r'^marker/(?P<radius>[\d]+)/', marker),
                        (r'^mapping/test.xml', kml_file),
                        #(r'^xml/country/(.*?)/?$', xml_resource),
                        
                        
                       (r'^dashboard/(?P<country>[-\w]+)/',country_page),
                       
                        (r'^mapping/',include('Ujima.mapping.urls')),
                       (r'^aid/',include('usaid.urls')),
                       (r'^arms/',include('weapons.urls')),
                         (r'^blog/', include('basic.blog.urls')),
                          (r'^dfid/',include('dfid.ukaid.urls')),
			(r'^flag/(?P<country>[-\w]+)/',country_flag),
                       (r'^admin/(.*)', admin.site.root),
                       (r'^Media/(?P<path>.*)', 'django.views.static.serve',\
     {'document_root': MEDIA_ROOT}),
     
                      
                         )
admin.autodiscover()


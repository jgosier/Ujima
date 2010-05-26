from django.conf.urls.defaults import *
from lobby.views import *


urlpatterns = patterns('',
                       (r'ujima/$',main),
                       (r'country/$', country_list),
                       (r'country/(?P<country>[-a-z]+)/$', country_detail),
                       (r'lobbytype/$', lobbytype_list),
                       (r'client/$', client_list),
                       (r'country/(?P<country>[-a-z]+)/(?P<year>\d+)/$',country_year),
                       (r'lobbytype/(?P<lobbytype>[-a-z]+)/$', lobbytype_detail),
                       (r'client/(?P<client>[-a-z]+)/$', client_detail),
                       (r'firm/$',firm_list),
                       (r'firms/(?P<firm>[-a-z]+)/$', firm_detail),
                       (r'search/$', search_detail),
                       
)


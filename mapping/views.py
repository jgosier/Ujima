from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from mapping.lib.marker import make_marker
from django.utils.safestring import mark_safe

#from django_restapi.model_resource import Collection
from django.utils.xmlutils import SimplerXMLGenerator
#from django_restapi.responder import XMLResponder
from weapons.arms.models import *
from Ujima.settings import map_production_key,map_development_key



def show(request):
    return render_to_response('mapping/show.html',locals())
"""
draw marker  given color,width and opacity
"""

def marker(request,radius=50,color='blue',opacity=1.0):
    radius = int(radius)
    stroke_width = 1
    # Defaults
    fill_color = color
    stroke_color = '#C32700'
    opacity = int(opacity)
    img=make_marker(radius,fill_color,stroke_color,stroke_width,opacity)
    response=HttpResponse(content_type='image/png')
    img.save(response, 'PNG')
    return response
def marker_size(request,country,app):
    return size
def locator_map(request,country):
    return img
def country_map(request,country):
    return map
def kml_file(request):
    
    kml=""" <citypop><city title="New York, N.Y." lat="40.714170" lng="-74.006390">
    <pop year="2004" value="8104079"/>
    <pop year="2000" value="8008278"/>
    <pop year="1990" value="7322564"/>
    </city>
    <city title="Los Angeles, Calif." lat="34.052220" lng="-118.242780">
    <pop year="2004" value="3845541"/>
    <pop year="2000" value="3694820"/>
    <pop year="1990" value="3485398"/>
    </city>
    <city title="Chicago, Ill." lat="41.850000" lng="-87.650000">
    <pop year="2004" value="2862244"/>
    <pop year="2000" value="2896016"/>
    <pop year="1990" value="2783726"/>
    </city>
    <city title="Houston, Tex." lat="29.763100" lng="-95.363100">
    <pop year="2004" value="2012626"/>
    <pop year="2000" value="1953631"/>
    <pop year="1990" value="1630553"/>
    </city>
    <city title="Philadelphia, Pa." lat="39.952200" lng="-75.164200">
    <pop year="2004" value="1470151"/>
    <pop year="2000" value="1517550"/>
    <pop year="1990" value="1585577"/>
    </city>
    <city title="Phoenix, Ariz." lat="33.448300" lng="-112.073300">
    <pop year="2004" value="1418041"/>
    <pop year="2000" value="1321045"/>
    <pop year="1990" value="983403"/>
    </city>
    <city title="San Diego, Calif." lat="37.715300" lng="-117.156400">
    <pop year="2004" value="1263756"/>
    <pop year="2000" value="1223400"/>
    <pop year="1990" value="1110549"/>
    </city>
    <city title="San Antonio, Tex." lat="29.423900" lng="-98.493300">
    <pop year="2004" value="1236249"/>
    <pop year="2000" value="1144646"/>
    <pop year="1990" value="935933"/>
    </city>
    <city title="Dallas, Tex." lat="32.783300" lng="-96.800000">
    <pop year="2004" value="1210393"/>
    <pop year="2000" value="1188580"/>
    <pop year="1990" value="1006877"/>
    </city>
    <city title="San Jose, Calif." lat="37.339400" lng="-121.893900">
    <pop year="2004" value="904522"/>
    <pop year="2000" value="894943"/>
    <pop year="1990" value="782248"/>
    </city>
    <city title="Detroit, Mich." lat="42.331400" lng="-83.045800">
    <pop year="2004" value="900198"/>
    <pop year="2000" value="951270"/>
    <pop year="1990" value="1027974"/>
    </city>
    <city title="Indianapolis, Ind." lat="39.768300" lng="-86.158100">
    <pop year="2004" value="784242"/>
    <pop year="2000" value="781870"/>
    <pop year="1990" value="741952"/>
    </city>
    <city title="Jacksonville, Fla." lat="30.331900" lng="-81.655800">
    <pop year="2004" value="777704"/>
    <pop year="2000" value="735617"/>
    <pop year="1990" value="635230"/>
    </city>
    <city title="San Francisco, Calif." lat="37.775000" lng="-122.418300">
    <pop year="2004" value="744230"/>
    <pop year="2000" value="776733"/>
    <pop year="1990" value="723959"/>
    </city>
    <city title="Columbus, Ohio" lat="39.961100" lng="-82.998900">
    <pop year="2004" value="730008"/>
    <pop year="2000" value="711470"/>
    <pop year="1990" value="632910"/>
    </city>
    </citypop>"""
    response=HttpResponse(mimetype='txt/xml')
    response.write(mark_safe(kml))
    return response
def draw_map(request,country):
    pass
def draw_map(request):
    from mapping.models import Country
    from django.db import connection
    from Ujima.usaid.aid.models import Country as ACountry
    
    cursor=connection.cursor()
    r=ACountry.objects.all().order_by('slug')
    aid={}
    points={}
    for country in r:
        cursor.execute("select year,sum(dollars)  from aid where PCountry='%s' group by year ;"%(country.code))
        aid[country.code]=list([[eval(x[0]),int(x[1])] for x in cursor.fetchall()]) 
    countries=Country.objects.filter(continent='AF')
    cursor.close()
    points={}
    key=map_production_key

    for contry in Country.objects.all():
        points[contry.iso_code]=contry.lat_lon()
    
    
    js="""
     
    """
    
    javascript2= mark_safe(js)
    return render_to_response('mapping/index.html',locals())

def country_page(request,country):
    from django.utils import simplejson
    from weapons.arms.models import Country as arms_country
    from Ujima.afJuma.afdb.models import Projcountry as afdb_country
    from dfid.ukaid.models import Country as dfid_country
    from Ujima.usaid.aid.models import Country as usaid_country
    from lobby.models import Country as lobby_country
    from Ujima.globalfund.models  import Country as globalfund_country
    from mapping.models import Country as mapping_country
    from django.db import connection
    countries=mapping_country.objects.filter(continent='AF')
    usaid={}
    data={}
    lobbying={}
    afdb={}
    dfid={}
    weapons={}
    globalfund={}
    country=str(country)
    cursor=connection.cursor()
    for cont in countries:
        try:
            c=arms_country.objects.get(slug=cont.slug())
            w={}
            cursor.execute("select year,sum(value) as value from  arms where country='%s' group by year;"%(c.countrycd))
            ress=list([[eval(x[0]),int(x[1])] for x in cursor.fetchall()])
            w["data"]=ress
            w["label"]=cont.name
            weapons[cont.slug()]=w
        except:
            
            weapons[cont.slug()]={}
        try:
            c=afdb_country.objects.get(slug=cont.slug())
            a={}
            cursor.execute("select Year,sum(TotalAmount)  from contract where ProjCountryCD='%s' group by year ;"%(c.countrycd))
            ress=list([[eval(x[0]),int(x[1])] for x in cursor.fetchall()])
            
            q={}
            
            a["data"]=ress
            a["label"]=cont.name
            afdb[cont.slug()]=a
            
        except:
            afdb[cont.slug()]={}
        try:
            c=dfid_country.objects.get(slug=cont.slug())
            d={}
            cursor.execute("select  YEAR,sum(LIFETIMEBUDGET) as amount from DFID where COUNTRY='%s' group by year ;"%(c.countrycd))
            ress=list([[eval(x[0]),int(x[1])] for x in cursor.fetchall()])
            
             
     
            d["data"]=ress
            d["label"]=cont.name
            dfid[cont.slug()]=d
            
        except:
            dfid[cont.slug()]={}
        try:
            c=usaid_country.objects.get(slug=cont.slug())
            u={}
            cursor.execute("select year,sum(dollars)  from aid where PCountry='%s' group by year ;"%(c.code))
            res=list([[eval(x[0]),int(x[1])] for x in cursor.fetchall()]) 
            u["data"]=res
            u["label"]=cont.name
            usaid[cont.slug()]=u
        except:
            usaid[cont.slug()]={}
        try:
            c=lobby_country.objects.get(slug=cont.slug())
            l={}
            cursor.execute("select year,sum(FINANCIAL_AMOUNT)  from activity where country='%s' and financial_amount>0 group by year;"%(c.country_cd))
            ress=list([[eval(x[0]),int(x[1])] for x in cursor.fetchall()]) 
            
            
            l["data"]=ress
            l["label"]=cont.name
            lobbying[cont.slug()]=l
        except:
            lobbying[cont.slug()]={}
            
        try:
            c=globalfund_country.objects.get(slug=cont.slug())
            g={}
            cursor.execute("select sum(DisbInUSD),GADisease  from fund where CountryCD='%s' group by GADisease;"%(c.countrycd))
            ress=list([[str(x[1]),int(x[0])] for x in cursor.fetchall()])
            
            ress[0][0]=1
            ress[1][0]=2
            ress[2][0]=3
            g["data"]=ress
            g["label"]=cont.name
            globalfund[cont.slug()]=g
        except:
            globalfund[cont.slug()]={}
  
    
    
    
    
    data["USAID"]=usaid
    data["LOBBYING"]=lobbying
    data["WEAPONS"]=weapons
    data["AFDB"]=afdb
    data["DFID"]=dfid
    data["GLOBALFUND"]=globalfund
    DATA=mark_safe(simplejson.dumps(data))
    cursor.close()
    return render_to_response('mapping/country_page.html',locals())
def application_page(request,application):
    return render_to_response('mapping/topic_page.html',locals())
def country_data(request,app,country):
    pass
    
    
    
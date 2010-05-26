from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect, \
    HttpResponseNotAllowed, Http404, HttpResponse, HttpResponseBadRequest, \
    HttpResponseNotFound, HttpResponseForbidden
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.utils.http import urlquote
from tagging.models import Tag, TaggedItem
from django.shortcuts import render_to_response
import urllib
import settings
from django.views.generic.list_detail import object_list
from basic.blog.models import *
from usaid.aid.models import *
from globalfund.models import *
import csv
from django.utils.safestring import mark_safe
import string
from django.utils import simplejson
from django.db import connection

from types import  NoneType
import datetime
from Ujima.main.forms import *
from django.template import RequestContext
#####boss search stuff

def simple_plot(request):
    
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter
    c = Country.objects.all().order_by('?')[:1].get()
    res=[]
    year=[]
    aids = Aid.objects.filter(pcountry=c)
    for aid in aids:
        res.append(aid.dollars)
        year.append(aid.datesigned)
    fig=Figure(facecolor="#f4faf6")
    fig.set_figsize_inches( ( 4.50 ,3.472) )
    ax=fig.add_subplot(111)
    ax.set_axis_bgcolor("#f4faf6")
    x=[]
    y=[]
    
    
    ax.plot_date(year, res, '.-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    ax.set_xlabel('date received', alpha=0.5)
    ax.set_ylabel('amount in Dollars', alpha=0.5)
    ax.set_title('Total amount of USAID tenders for work in '+c.country)



    fig.autofmt_xdate()
    

    canvas=FigureCanvas(fig)
    response=HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response


def aid_json():
    from Ujima.usaid.aid.models import Country
    country = Country.objects.all().order_by('?')[:1].get()
    cursor=connection.cursor()
    result=[]
    cursor.execute("select year,sum(dollars)  from aid where PCountry='%s' group by year ;"%(country.code))
    res=list([[eval(x[0]),int(x[1])] for x in cursor.fetchall()]) 
    result.append(list((country.country,country.slug)))
    result.append(res)
    
    return list(result)
    #return mark_safe(simplejson.dumps(list(result))) 
def aid_map():
    from Ujima.usaid.aid.models import Country
    r=Country.objects.all()
    result=[]
    for country in r:
    #c = Country.objects.get(slug=country.slug)
        cursor=connection.cursor()
        cursor.execute("select FORMAT((sum(dollars)/1000000),2)   from aid where PCountry='%s' and year='2008' ;"%(country.code))
        x=list(cursor.fetchone())
        if(type(x[0]) is not NoneType ): 
            res=list([[str(country.country),float(x[0])] ])
            result.append(res[0])
     

    return mark_safe(simplejson.dumps(result))

    
def ukaid_map_json():
    
    from dfid.ukaid.models import *
    r=Country.objects.all()
    result=[]
    for country in r:
    #c = Country.objects.get(slug=country.slug)
        cursor=connection.cursor()
        cursor.execute("select  FORMAT((sum(LIFETIMEBUDGET)/1000000),2) from DFID where country='%s' and year='2008' ;"%(country.countrycd))
        x=list(cursor.fetchone())
        if(type(x[0]) is not NoneType ):
            res=list([[str(country.country),float(x[0])] ])
            result.append(res[0])
     

    return mark_safe(simplejson.dumps(result)) 
from django.shortcuts import render_to_response
from django.template import RequestContext


   
def index(request,template):
    from mapping.models import Country
    countries=Country.objects.filter(continent='AF')
    
    cat=Category.objects.all()
    posts = Post.objects.published()[:2]
    jshawn=aid_json()
    a_map=aid_map()
    a_uk=ukaid_map_json()
    a_rand=aid_json()
    country=a_rand[0][0]
    data=[]
    data.append(a_rand[1])
    return render_to_response(template,locals(),context_instance=RequestContext(request))




       
def blog(request,template):
    return render_to_response(template,locals())
def faq(request,template):
    return render_to_response(template,locals())
def contact(request,template):
    return render_to_response(template,locals())
def about(request,template):
    return render_to_response(template,locals())
def error_page(request,template):
	return render_to_response(template,locals)
def lobby_main(request,template):
	return render_to_response(template,locals())
def funding_main(request,template):
	return render_to_response(template,locals())
def weapons_main(request,template):
	return render_to_response(template,locals())
def aid_main(request,template):
	return render_to_response(template,locals())

def download_csv(request,query):
    response = HttpResponse(mimetype='text/csv', content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename=ujima_%s.csv' % query
    #######get query
    ###return a list of results
    writer = csv.writer(response, quoting=csv.QUOTE_ALL)
    for object in list:
        #object.replace('\n',' ').replace('\r','')),
        writer.writerow(object)
    return response



def get_lat_long(location):
    """method to get a latitude and longititude given a location"""
    key = settings.GOOGLE_API_KEY
    output = "csv"
    location = urllib.quote_plus(location)
    request = "http://maps.google.com/maps/geo?q=%s&output=%s&key=%s" % (location, output, key)
    data = urllib.urlopen(request).read()
    dlist = data.split(',')
    if dlist[0] == '200':
        return "%s, %s" % (dlist[2], dlist[3])
    else:
        return ''
 
def render_map(request, div_id,location):
    lat,long=get_lat_long(location)
    js = '''
        </script>
        <script type="text/javascript">
            //<![CDATA[
            var %(name)s_marker ;
            $(document).ready(function () {
                if (GBrowserIsCompatible()) {
                    var map = new GMap2(document.getElementById("%s"));
                    map.setCenter(new GLatLng(%s,%s), 13);
                    %(name)s_marker = new GMarker(new GLatLng(4.735543142197098,-74.0822696685791), {draggable: true});
                    map.addOverlay(%(name)s_marker);
                    map.addControl(new GLargeMapControl());
                    $('#%(name)s_id')[0].value = %(name)s_marker.getLatLng().lat() + "," + %(name)s_marker.getLatLng().lng();
                    GEvent.addListener(%(name)s_marker, "dragend", function() {
                        var point = %(name)s_marker.getLatLng();
                        $('#%(name)s_id')[0].value = point.lat() + "," + point.lng();
                    });
                }});
            $(document).unload(function () {GUnload()});
            //]]>
        </script>
        ''' % (div_id,lat,long)
    html = self.inner_widget.render("%s" % name, None, dict(id='%s_id' % name))
    html += "<div id=\"map_%s\" style=\"width: 600px; height: 300px\"></div>" % name
    return mark_safe(js+html)
 
###################################################################
####ajax object search  ##########################################   
class JsonResponse(HttpResponse):
    def __init__(self, obj):
        self.original_obj = obj
        HttpResponse.__init__(self, self.serialize())
        self["Content-Type"] = "text/javascript"

def json_lookup(request, queryset, field, limit=10, login_required=False):
    import string
    """
    Method to lookup a model field and return a array. Intended for use 
    in AJAX widgets.
    """
    if login_required and not request.user.is_authenticated():
        return redirect_to_login(request.path)
    obj_list = []
    lookup = {
        '%s__istartswith' % field: request.GET['q'],
    }
    for obj in queryset.filter(**lookup)[:limit]:
        obj_list.append(getattr(obj, field))
    ##obj_list=" ".join(obj_list)
    return HttpResponse("\n".join(obj_list))
def export(request,model,app):
    
    p={'country':'Country','firm':'Lobbyist','client':'Clients',\
       'lobbytype':'Lobbytype','disease':'Disease','orgtype':'Orgtype',\
       'region':'Region','product':'Prodcode','vendor':'Vendors','weapon':'Weapon'}   
    
    model=p[str(model)]
    if(app=="lobby"):from Ujima.lobby.models import *
    if(app=="globalfund"):from  Ujima.globalfund.models import *
    if(app=="arms"):from weapons.arms.models import *
    if(app=="aid"):from usaid.aid.models import *
   
    model=eval(model)
    
    
    from django.template.defaultfilters import slugify
    ##c = Country.objects.get(slug='angola')
    query = model.objects.all()
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % slugify(model.__name__)
    writer = csv.writer(response)
    # Write headers to CSV file
    headers = []
    for field in model._meta.fields:
        headers.append(field.name)
    writer.writerow(headers)
    # Write data to CSV file
    print query
    for obj in query:
        row = []
        for field in model._meta.fields:
            row.append(getattr(obj, field.name))
        writer.writerow(row)
    # Return CSV file to browser as download
    return response
def export2(request,model,app,slug):
    from django.template.defaultfilters import slugify
    p={'country':'Country','firm':'Lobbyist','client':'Clients',\
       'lobbytype':'Lobbytype','disease':'Disease','orgtype':'Orgtype',\
       'region':'Region','product':'Prodcode','vendor':'Vendors','weapon':'Weapon'}   
    
   
   
    mod=model
    slug=str(slug)
    
    if(app=="lobby"):
	from Ujima.lobby.models import *
        model=eval(p[str(model)])
	nm="activity_for_"
	meta=['Firm','Client','Country','Amount','Description','Type Of Lobbying','Year']
	if(mod=="country"):
		c = Country.objects.get(slug=slug)
    		lobbyists = Activity.objects.filter(country=c)
		con=lobbyists[0].country.country
	if(mod=="lobbytype"):
		c = Lobbytype.objects.get(slug=slug)
    		lobbyists = Activity.objects.filter(act_type=c)
                con=c.name
	if(mod=="client"):
		c = Clients.objects.get(slug=slug)
    		lobbyists = Activity.objects.filter(fp_cd=c)
		con=c.name
	if(mod=="firm"):
		f = Lobbyist.objects.get(slug=slug)
    		lobbyists = Activity.objects.filter(reg_cd=f)
        res=[[lobbyist.reg_cd.name,lobbyist.fp_cd.name,lobbyist.country.country,lobbyist.financial_amount,lobbyist.activity_desc,lobbyist.act_type,lobbyist.year] for lobbyist in lobbyists]
	
		
    if(app=="globalfund"):
	from  Ujima.globalfund.models import *
	model=eval(p[str(model)])
	nm="funding_for_"
	meta=['Organization','Country','Amount','Region','Start Date','End Date','Disease']
	if(mod=="country"):
		c = Country.objects.get(slug=slug)
    		fund = Fund.objects.filter(countrycd=c)
                con=c.country
        if(mod=="region"):
		f = Region.objects.get(slug=slug)
    		fund = Fund.objects.filter(regioncd=f)
		con=f.name
	if(mod=="disease"):
        	d = Disease.objects.get(slug=slug)
    		fund = Fund.objects.filter(gadisease=d)
		con=d.name
	if(mod=="orgtype"):
		o = Orgtype.objects.get(slug=slug)
    		fund = Fund.objects.filter(prtype=o)
		con=o.name
	res=[[fund.org,fund.countrycd.country,fund.disbinusd,fund.regioncd.region,fund.periodstartdate,fund.periodenddate,fund.gadisease] for fund in fund]
		
    if(app=="arms"):
	from weapons.arms.models import *
	model=eval(p[str(model)])
	nm="weapons_for_"
	meta=['Weapon','Quantity','Amount(USD)','Year']
	if(mod=='weapon'):
		w = Weapon.objects.get(slug=slug)
    		arms = Arms.objects.filter(catcode=w)
		con=w.slug
	if(mod=='country'):
		c = Country.objects.get(slug=slug)
    		arms = Arms.objects.filter(country=c)
		con=c.country
	res=[[arms.catcode,arms.quantity,arms.value,arms.year] for arms in arms]
    if(app=="aid"):
	from usaid.aid.models import *
	model=eval(p[str(model)])
	nm="aid_for_"
	meta=['Vendor','Country','Amount(USD)','Agency','Description','Year','Product or Service']
	if(mod=='country'):
		c = Country.objects.get(slug=slug)
    		aid = Aid.objects.filter(pcountry=c)
		con=c.slug
	if(mod=='product'):
		c = Prodcode.objects.get(slug=slug)
    		aid = Aid.objects.filter(prodcode=c)
		con=c.slug
     	if(mod=='vendor'):
		v = Vendors.objects.get(slug=slug)
    		aid = Aid.objects.filter(duns=v)
		v.name
	res=[[aid.vendor,aid.pcountry,aid.dollars,aid.agency,aid.description,aid.year,aid.prodcode] for aid in aid]

   
    
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s%s.csv' % (nm,slugify(con))
    writer = csv.writer(response)
    writer.writerow(meta)
    for b in res:
	writer.writerow(b)
    return response
def sorted_countries(country_list):
    
        #listt.sort()
    countries={}
    listing=[]
    for i in range(0,len(country_list)):
        cont=country_list[i]
        starter=str(cont.country[0])
        if not starter in countries.keys():
            countries[starter]=[cont]
            
        else:
            x=countries[starter]
            x.append(cont)
            countries[starter]=x
    
    #countries.sort()         
    p=countries.keys()
    p.sort()
    q=countries.values()
    z=[]
    for i in range(0,len(p)):
        z.append([p[i],countries[p[i]]])
    return z

        
def google_search(request):
    
    mutable_get = request.GET.copy()
    if 'cof' in mutable_get:
        del mutable_get['cof']
    return render_to_response('gsearch.html', RequestContext(request, {
        'query': request.GET.get('q'),
        'query_string': mutable_get.urlencode(),
        
    }))
        
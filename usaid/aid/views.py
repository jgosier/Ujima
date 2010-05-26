from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from Ujima.usaid.aid.models import *
from django.utils.safestring import mark_safe
from main.views import sorted_countries






def country_list(request):
    
    import string
    from django.utils import simplejson
    from django.db import connection

    r=Country.objects.all().order_by('slug')
    country_dict=sorted_countries(r)
    
    result={}
    th=[]
    
    
    for country in r:
    #c = Country.objects.get(slug=country.slug)
        cursor=connection.cursor()
        cursor.execute("select year,sum(dollars)  from aid where PCountry='%s' group by year ;"%(country.code))
        res=list([[eval(x[0]),int(x[1])] for x in cursor.fetchall()]) 
        result[str(country.slug)]={'label':country.country,'data':res}
        if(country.country=="Central African Republic"):
            xcountry="the_Central_African_Republic"
        elif(country.slug=="comoros"):
            xcountry="the_Comoros"
        elif(country.slug=="congo-brazzaville"):
            xcountry="the_Republic_of_the_Congo"
        elif(country.slug=="congo-kinshasa"):
            xcountry="the_Democratic_Republic_of_the_Congo"
    
    
        else:
            xcountry=country.country 
        th.append((country.slug,country.country,xcountry))

    sorted_result=sorted(result) 
    t=mark_safe(simplejson.dumps(result))
    tr=mark_safe(simplejson.dumps(th))
    
    return render_to_response('aid/countries.html',{'country_list':r,'res':t,'con':tr,'country_dict':country_dict})

   

def vendor_list(request):
    d = Vendors.objects.all()
    return render_to_response('aid/vendor.html',{'vendor_list':d},context_instance=RequestContext(request))

def prod_list(request):
    p = Prodcode.objects.all()
    return render_to_response('aid/product.html',{'prod_list':p},context_instance=RequestContext(request))

def search_detail(request):
    if 'q' in request.GET:
        q = request.GET['q']
        search_results = Aid.objects.filter(duns__name__icontains=q)
    else:
        q = None
        search_results = None
    return render_to_response('aid/search_detail.html',
                {'search_results': search_results, 'query': q},context_instance=RequestContext(request))

def country_detail(request, country):
    count=[]
    
    c = Country.objects.get(slug=country)
    if(c.country=="Central African Republic"):
        xcountry="CentralAfricanRepublic"
    elif(c.slug=="comoros"):
        xcountry="Comoros"
    elif(c.slug=="congo-brazzaville"):
        xcountry="RepubliqueDuCongo"
    elif(c.slug=="congo-kinshasa"):
        xcountry="DRCongo"
    elif(c.slug=="cote-divoire"):
        xcountry="CotedIvoire"
    else:
        xcountry=c.country 
        
    aid = Aid.objects.filter(pcountry=c)
    y = Aid.objects.filter(pcountry=c).values('year').distinct().order_by('year')
    years = []
    for yr in y:
        years.append(yr['year'])
    return render_to_response('aid/country_detail.html',{'country':c,'cont':xcountry,
'aid':aid, 'years': years}, context_instance=RequestContext(request))

def prod_detail(request, prodcode):
    c = Prodcode.objects.get(slug=prodcode)
    aid = Aid.objects.filter(prodcode=c)
    return render_to_response('aid/product_detail.html',{'prodcode':c,
'aid':aid},context_instance=RequestContext(request))

def vendor_detail(request, vendors):
    v = Vendors.objects.get(slug=vendors)
    aid = Aid.objects.filter(duns=v)
    return render_to_response('aid/vendor_detail.html',{'vendors':v,
'aid':aid},context_instance=RequestContext(request))


def country_year(request, country, year):
    c = Country.objects.get(slug=country)
    aid = Aid.objects.filter(pcountry=c, year=year)
    return render_to_response('aid/country_year.html',{'country':c,
'aid':aid, 'year': year},context_instance=RequestContext(request))






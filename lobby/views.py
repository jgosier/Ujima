from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from lobby.models import *
from django.utils.safestring import mark_safe
from main.views import sorted_countries


def main(request):
    return render_to_response("base.html")
def country_list(request):
    
    import string
    from Ujima.lobby.models import Country,Activity
    from django.utils import simplejson
    from django.db import connection

    r=Country.objects.all().order_by('slug')
    country_dict=sorted_countries(r)
    result={}
    th=[]
    
    
    for country in r:
	#c = Country.objects.get(slug=country.slug)
        cursor=connection.cursor()
	cursor.execute("select year,sum(financial_amount)  from activity where country='%s' and financial_amount>0 group by year order by year;"%(country.country_cd))
	res=list([[eval(x[0]),int(x[1])] for x in cursor.fetchall()])
	if(country.country=="Central African Republic"):
		xcountry="the_Central_African_Republic"
	elif(country.slug=="comoro-islands"):
		xcountry="the_Comoros"
	elif(country.slug=="congo-brazzaville"):
		xcountry="the_Republic_of_the_Congo"
	elif(country.slug=="congo-kinshasa-zaire"):
		xcountry="the_Democratic_Republic_of_the_Congo"
	elif(country.slug=="cote-divoire-ivory-coast"):
		xcountry="Cote_d'Ivoire"
	elif(country.slug=="saharawi-arab-democratic-republic"):
		xcountry="Western_Sahara"
	elif(country.slug=="sao-tome-and-principe"):
		xcountry="Sao_Tome_and_Principe"
	elif(country.slug=="seychelles"):
		xcountry="the_Seychelles"
	elif(country.slug=="southwest-africa"):
		xcountry="Namibia"
	elif(country.slug=="spanish-sahara"):
		xcountry="Western_Sahara"
	elif(country.slug=="dahomey"):
		xcountry="Benin"
	elif(country.slug=="gambia"):
		xcountry="The_Gambia"
	elif(country.slug=="somali-democratic-republic"):
		xcountry="Somalia"
	
	else:
    		xcountry=country.country 
	result[str(country.slug)]={'label':country.country,'data':res}
        th.append((country.slug,country.country,xcountry))

    sorted_result=sorted(result)
   
	 
    t=mark_safe(simplejson.dumps(result))
    tr=mark_safe(simplejson.dumps(th))
    return render_to_response('country/countries.html',{'country_list':r,'res':t,'con':tr,'country_dict':country_dict})

def country_detail(request, country):
    c = Country.objects.get(slug=country)
    lobbyists = Activity.objects.filter(country=c)
    y = Activity.objects.filter(country=c).values('year').distinct().order_by('year')
    years = []
    for yr in y:
        years.append(yr['year'])
    return render_to_response('country/country_detail.html',{'country':c,
'lobbyists':lobbyists, 'years': years}, context_instance=RequestContext(request))

def lobbytype_list(request):
    a = Lobbytype.objects.all()
    return render_to_response('country/lobbytype.html',{'lobbytype_list':a},context_instance=RequestContext(request))


def client_list(request):
    k = Clients.objects.all()
    return render_to_response('country/client.html',{'client_list':k},context_instance=RequestContext(request))

def firm_list(request):
    f = Lobbyist.objects.all()
    return render_to_response('country/firm.html',{'firm_list':f},context_instance=RequestContext(request))

def country_year(request, country, year):
    c = Country.objects.get(slug=country)
    lobbyists = Activity.objects.filter(country=c, year=year)
    return render_to_response('country/country_year.html',{'country':c,
'lobbyists':lobbyists, 'year': year},context_instance=RequestContext(request))


def lobbytype_detail(request, lobbytype):
    c = Lobbytype.objects.get(slug=lobbytype)
    lobbyists = Activity.objects.filter(act_type=c.name)
    return render_to_response('country/lobbytype_detail.html',{'lobbytype':c,
'lobbyists':lobbyists},context_instance=RequestContext(request))


def client_detail(request, client):
    c = Clients.objects.get(slug=client)
    lobbyists = Activity.objects.filter(fp_cd=c)
    return render_to_response('country/client_detail.html',{'client':c,
'lobbyists':lobbyists},context_instance=RequestContext(request))


def firm_detail(request, firm):
    f = Lobbyist.objects.get(slug=firm)
    lobbyists = Activity.objects.filter(reg_cd=f)
    return render_to_response('country/firm_detail.html',{'firm':f,
'lobbyists':lobbyists},context_instance=RequestContext(request))

def search_detail(request):
    if 'q' in request.GET:
        q = request.GET['q']
        search_results = Activity.objects.filter(country__country__icontains=q)
    else:
        q = None
        search_results = None
    return render_to_response('country/search_detail.html',
                {'search_results': search_results, 'query': q},context_instance=RequestContext(request) )

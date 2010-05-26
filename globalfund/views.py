from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from Ujima.globalfund.models import *


def country_list(request):
    from main.views import sorted_countries
    
   
    r = Country.objects.all()
    country_dict=sorted_countries(r)
    return render_to_response('globalfund/countries.html',{'country_list':r,'country_dict':country_dict})

def disease_list(request):
    d = Disease.objects.all()
    return render_to_response('globalfund/disease.html',{'disease_list':d})

def region_list(request):
    g = Region.objects.all()
    return render_to_response('globalfund/region.html',{'region_list':g})

def orgtype_list(request):
    o = Orgtype.objects.all()
    return render_to_response('globalfund/orgtype.html',{'orgtype_list':o})


def country_detail(request, country):
    
    c = Country.objects.get(slug=country)
    fund = Fund.objects.filter(countrycd=c)
    return render_to_response('globalfund/country_detail.html',{'country':c,
'fund':fund},context_instance=RequestContext(request))


def region_detail(request, region):
    f = Region.objects.get(slug=region)
    fund = Fund.objects.filter(regioncd=f)
    return render_to_response('globalfund/region_detail.html',{'region':f,
'fund':fund}, context_instance=RequestContext(request))


def disease_detail(request, disease):
    d = Disease.objects.get(slug=disease)
    fund = Fund.objects.filter(gadisease=d)
    return render_to_response('globalfund/disease_detail.html',{'disease':d,
'fund':fund},context_instance=RequestContext(request))

def orgtype_detail(request, orgtype):
    o = Orgtype.objects.get(slug=orgtype)
    fund = Fund.objects.filter(prtype=o)
    return render_to_response('globalfund/orgtype_detail.html',{'orgtype':o,
'fund':fund},context_instance=RequestContext(request))


def orgsearch_detail(request):
    if 'q' in request.GET:
        q = request.GET['q']
        orgsearch_results = Fund.objects.filter(org__orgname__icontains=q)
    else:
        q = None
        orgsearch_results = None
    return render_to_response('globalfund/orgsearch_detail.html',
                {'orgsearch_results': orgsearch_results, 'query': q},context_instance=RequestContext(request))




from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from dfid.ukaid.models import *
from main.views import sorted_countries
def country_list(request):
    r = Country.objects.all()
    country_dict=sorted_countries(r)
    return render_to_response('ukaid/countries.html',{'country_list':r,'country_dict':country_dict})

def project_list(request):
    d = Projects.objects.all()
    return render_to_response('ukaid/projects.html',{'project_list':d})

def risk_list(request):
    p = Risk.objects.all()
    return render_to_response('ukaid/risk.html',{'risk_list':p})

def type_list(request):
    r = Typefunding.objects.all()
    return render_to_response('ukaid/type.html',{'type_list':r})

def search_detail(request):
    if 'q' in request.GET:
        q = request.GET['q']
        search_results = Dfid.objects.filter(ariescode__projecttitle__icontains=q)
    else:
        q = None
        search_results = None
    return render_to_response('ukaid/search_detail.html',
                {'search_results': search_results, 'query': q},context_instance=RequestContext(request))

def country_detail(request, country):
    c = Country.objects.get(slug=country)
    dfid = Dfid.objects.filter(country=c)
    y = Dfid.objects.filter(country=c).values('year').distinct().order_by('year')
    years = []
    for yr in y:
        years.append(yr['year'])
    return render_to_response('ukaid/country_detail.html',{'country':c,
'dfid':dfid, 'years': years}, context_instance=RequestContext(request))

def type_detail(request, typefunding):
    c = Typefunding.objects.get(slug=fundnature)
    dfid = dfid.objects.filter(fundnature=c)
    return render_to_response('ukaid/type_detail.html',{'typefunding':c,
'dfid':dfid},context_instance=RequestContext(request))

def risk_detail(request, risk):
    v = Risk.objects.get(slug=risk)
    dfid = Dfid.objects.filter(risk=v)
    return render_to_response('ukaid/risk_detail.html',{'risk':v,
'dfid':dfid},context_instance=RequestContext(request))


def country_year(request, country, year):
    c = Country.objects.get(slug=country)
    dfid = Dfid.objects.filter(country=c, year=year)
    return render_to_response('ukaid/country_year.html',{'country':c,
'dfid':dfid, 'year': year},context_instance=RequestContext(request))

def project_detail(request, projects):
    v = Projects.objects.get(slug=projects)
    dfid = Dfid.objects.filter(ariescode=v)
    return render_to_response('ukaid/project_detail.html',{'projects':v,
'dfid':dfid},context_instance=RequestContext(request))

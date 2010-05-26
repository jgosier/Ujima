from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from Ujima.afJuma.afdb.models import *
def sorted_countries(country_list):
    
        #listt.sort()
    countries={}
    listing=[]
    for i in range(0,len(country_list)):
        cont=country_list[i]
        try:
            starter=str(cont.biddercountry[0])
        except:
            starter=str(cont.projectcountry[0])
            
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

        

def bcountry_list(request):
    r = Bidcountry.objects.all()
    country_dict=sorted_countries(r)
    return render_to_response('bank/bcountries.html',{'bcountry_list':r,'country_dict':country_dict})

def pcountry_list(request):
    s = Projcountry.objects.all()
    country_dict=sorted_countries(s)
    return render_to_response('bank/pcountries.html',{'pcountry_list':s,'country_dict':country_dict})


def bidder_list(request):
    d = Bidders.objects.all()
    return render_to_response('bank/bidder.html',{'bidder_list':d}, context_instance=RequestContext(request))
def bidder_detail(request,bidder):
    d = Bidders.objects.get(slug=bidder)
    contract=Contract.objects.filter(biddercod=d)
    y = Contract.objects.filter(biddercod=d).values('year').distinct().order_by('year')
    years = []
    for yr in y:
        years.append(yr['year'])
    return render_to_response('bank/bidder_detail.html',{'pcountry':d,
'contract':contract, 'years': years}, context_instance=RequestContext(request))
def proc_list(request):
    p = Procuremode.objects.all()
    return render_to_response('bank/proc.html',{'proc_list':p}, context_instance=RequestContext(request))
def procuremode(request,mode):
    p = Procuremode.objects.get(slug=mode)
    contract=Contract.objects.filter(procmode=p)
    y = Contract.objects.filter(procmode=p).values('year').distinct().order_by('year')
    years = []
    for yr in y:
        years.append(yr['year'])
    return render_to_response('bank/proc_detail.html',{'pcountry':p,
'contract':contract, 'years': years}, context_instance=RequestContext(request))
    

def expense_list(request):
    p = Expensecode.objects.all()
    return render_to_response('bank/expense.html',{'expense_list':p})
def expense_detail(request,expense):
    expense=str(expense)
    ed=Expensecode.objects.get(slug=expense)
    contract=Contract.objects.filter(expensecode=ed)
    y = Contract.objects.filter(expensecode=ed).values('year').distinct().order_by('year')
    years = []
    for yr in y:
        years.append(yr['year'])
    return render_to_response('bank/expense_detail.html',{'pcountry':"",
'contract':contract, 'years': years}, context_instance=RequestContext(request))
def pcountry_detail(request, pcountry):
    pcountry=str(pcountry)
    c = Projcountry.objects.get(slug=pcountry)
    contract = Contract.objects.filter(projcountrycd=c)
    y = Contract.objects.filter(projcountrycd=c).values('year').distinct().order_by('year')
    years = []
    for yr in y:
        years.append(yr['year'])
    return render_to_response('bank/pcountry_detail.html',{'pcountry':c.projectcountry,
'contract':contract, 'years': years}, context_instance=RequestContext(request))
def bcountry_detail(request, bcountry):
    r = Bidcountry.objects.get(slug=bcountry)
    
    contract = Contract.objects.filter(bidcountrycd=r)
    y = Contract.objects.filter(bidcountrycd=r).values('year').distinct().order_by('year')
    years = []
    for yr in y:
        years.append(yr['year'])
    return render_to_response('bank/bcountry_detail.html',{'bcountry':r.biddercountry,
'contract':contract, 'years': years}, context_instance=RequestContext(request))
def bcountry_year(request, bcountry,year):
    r = Bidcountry.objects.get(slug=bcountry) 
    contract = Contract.objects.filter(bidcountrycd=r,year=year)
    y = Contract.objects.filter(bidcountrycd=r).values('year').distinct().order_by('year')
    return render_to_response('bank/bcountry_detail.html',{'bcountry':r.biddercountry,
'contract':contract, 'years': years}, context_instance=RequestContext(request))
def pcountry_year(request, pcountry,year):
    pcountry=str(pcountry)
    c = Projcountry.objects.get(slug=pcountry)
    contract = Contract.objects.filter(projcountrycd=c,year=year)
    y = Contract.objects.filter(projcountrycd=c).values('year').distinct().order_by('year')
    years = []
    for yr in y:
        years.append(yr['year'])
    return render_to_response('bank/pcountry_detail.html',{'pcountry':c.projectcountry,
'contract':contract, 'years': years}, context_instance=RequestContext(request))
def bidder_year(request,bidder,year):
    d = Bidders.objects.get(slug=bidder)
    contract=Contract.objects.filter(biddercod=d,year=year)
    years=[]
    return render_to_response('bank/bidder_detail.html',{'pcountry':d,
'contract':contract, 'years': years}, context_instance=RequestContext(request))
    
def country_flag(request,country):
    if(country=="centrafrique" ):
        cont="the_Central_African_Republic"
    elif(country=="congo-cg" ):
        cont="the_Republic_of_the_Congo"
    elif(country=="dem-rep-congo" ):
        cont="the_Democratic_Republic_of_the_Congo"
    elif(country=="cote-divoire"):
        cont="Cote_d'Ivoire"
    elif(country=="gambia"):
        cont="The_Gambia"
    elif(country=="sao-tome"):
        cont="Sao_Tome_and_Principe"
    elif(country=="china"):
        cont="the_People's_Republic_of_China"
    elif(country=="comoros"):
        cont="the_Comoros"
    elif(country=="netherlands"):
        cont="the_Netherlands"
    elif(country=="united-states"):
        cont="the_United_States"
    elif(country=="united-kingdom"):
        cont="the_United_Kingdom"
    elif(country=="algeria"):
        cont="Algeria"
    else:
        cont=Bidcountry.objects.get(slug=country).biddercountry
    res=("http://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Flag_of_%s.svg/125px-Flag_of_%s.svg.png") %(cont,cont)
    return  HttpResponseRedirect(res) 
def search_detail(request):
    if 'q' in request.GET:
        q = request.GET['q']
        search_results =  Contract.objects.filter(country__country__icontains=q)
    else:
        q = None
        search_results = None
    return render_to_response('country/search_detail.html',
                {'search_results': search_results, 'query': q},context_instance=RequestContext(request) )





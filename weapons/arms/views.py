from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from weapons.arms.models import *
from main.views import sorted_countries

def country_list(request):
    r = Country.objects.all()
    country_dict=sorted_countries(r)
    
    return render_to_response('arms/countries.html',{'country_list':r,'country_dict':country_dict})
def country_flag(request,country):
    
    country=str(country)
    if(country=="central-african-republic" or country=="central-africa-regional"):
        cont="the_Central_African_Republic"
    elif(country=="comoros" or country=="comoro-islands"):
        cont="the_Comoros"
    elif(country=="congo-republic-of-the" or country=="congo-brazzaville"):
        cont="the_Republic_of_the_Congo"
    elif(country=="congo-democratic-republic-of-the" or country=="congo-kinshasa-zaire" or country=="congo-dem-rep"):
        cont="the_Democratic_Republic_of_the_Congo"
    elif(country=="zanzibar-tanzania"):
        cont="Zanzibar"
    elif(country=="gambia"):
        cont="The_Gambia"
    elif(country=="cote-divoire-ivory-coast"or country=="cote-divoire"):
        cont="Cote_d'Ivoire"
    elif(country=="saharawi-arab-democratic-republic"):
        cont="Western_Sahara"
    elif(country=="sao-tome-and-principe"):
        cont="Sao_Tome_and_Principe"
    elif(country=="seychelles"):
        cont="the_Seychelles"
    elif(country=="southwest-africa"):
        cont="Namibia"
    elif(country=="spanish-sahara"):
        cont="Western_Sahara"
    elif(country=="dahomey"):
        cont="Benin"
    elif(country=="north-africa-regional"):
        cont="Western_Sahara"
    elif(country=="francophone-africa"):
        cont="Algeria"
    elif(country=="east-african-community"):
        cont="EAC"
    elif(country=="st-helena"):
        cont="Saint_Helena"
    elif(country=="africa-regional"):
        cont="Benin"
    
    elif(country=="tristan-da-cunha"):
        cont="Tristan_da_Cunha"
    elif(country=="ascension-island"):
        cont="the_United_Kingdom"
    elif(country=="gambia"or country=="gambia-the"):
        cont="The_Gambia"
    elif(country=="somali-democratic-republic" or country=="somalia" or country=="somali-democratic-rep"):
        cont="Somalia"
    elif(country=="south-africa-republic-of"):
        cont="South_Africa"
    elif(country=="angola"):
        cont="Angola"
       
    else:
        from lobby.models import  Country
        cont=Country.objects.get(slug=country).country
    res=("http://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Flag_of_%s.svg/125px-Flag_of_%s.svg.png") %(cont,cont)
    return  HttpResponseRedirect(res) 
    
def weapons_list(request):
    d = Weapon.objects.all()
    return render_to_response('arms/weapon.html',{'weapons_list':d})

def country_detail(request, country):
    c = Country.objects.get(slug=country)
    arms = Arms.objects.filter(country=c)
    return render_to_response('arms/country_detail.html',{'country':c,
'arms':arms},context_instance=RequestContext(request))


def weapon_detail(request, weapon):
    w = Weapon.objects.get(slug=weapon)
    arms = Arms.objects.filter(catcode=w)
    return render_to_response('arms/weapon_detail.html',{'weapon':w,
'arms':arms},context_instance=RequestContext(request))


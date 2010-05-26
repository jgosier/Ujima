from django.contrib import admin
from world.models import Language, Country, FirstAdministrativeArea, SecondAdministrativeArea, Country, Place

class LanguageAdmin(admin.ModelAdmin):
    search_fields = ('iso3_code', 'iso2_code', 'iso1_code', 'name',)
    ordering = ('name',)
    list_display = ('iso3_code', 'iso2_code', 'iso1_code', 'name',)
    
class CountryAdmin(admin.ModelAdmin):
    search_fields = ('iso_code', 'iso3_code', 'name',)
    ordering = ('name',)
    list_filter = ('continent',)
    list_display = ('iso_code', 'name', 'population', 'area',)

class FirstAdministrativeAreaAdmin(admin.ModelAdmin):
    search_fields = ('code', 'name',)
    ordering = ('code',)
    list_display = ('code', 'name',)

class SecondAdministrativeAreaAdmin(admin.ModelAdmin):
    search_fields = ('code', 'name',)
    ordering = ('code',)
    list_display = ('code', 'name',)

class PlaceAdmin(admin.ModelAdmin):
    search_fields = ('name', 'ascii_name',)
    ordering = ('name',)
    list_display = ('name', 'ascii_name', 'country', 'population', 'elevation', 'timezone')
    
    

admin.site.register(Language, LanguageAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(FirstAdministrativeArea, FirstAdministrativeAreaAdmin)
admin.site.register(SecondAdministrativeArea, SecondAdministrativeAreaAdmin)
admin.site.register(Place, PlaceAdmin)
from django.contrib import admin
from Ujima.globalfund.models import *
class DiseaseAdmin(admin.ModelAdmin):
    list_display =('gadisease','disease','slug')
    search_fields = ('slug','disease','gadisese')
    
admin.site.register(Disease,DiseaseAdmin)
class OrgsAdmin(admin.ModelAdmin):
    list_display =('orgcd','orgname','slug')
    search_fields = ('orgcd','orgname','slug')
    

admin.site.register(Orgs,OrgsAdmin)
class OrgtypeAdmin(admin.ModelAdmin):
    list_display =('prtype','orgtype','slug')
    search_fields = ('prtype','orgtype','slug')
    

admin.site.register(Orgtype,OrgtypeAdmin)
class RegionAdmin(admin.ModelAdmin):
    list_display =('regioncd','region','slug')
    search_fields = ('regioncd','region','slug')
    

admin.site.register(Region,RegionAdmin)
class FundAdmin(admin.ModelAdmin):
    list_display =('gdcd','regioncd','round','org','gddate','gagrantno','disbno','disbinusd',\
                   'disbineur','disbineg','prtype','gfrating','periodstartdate','periodenddate','gadisease','countrycd')

    

admin.site.register(Fund,FundAdmin)   


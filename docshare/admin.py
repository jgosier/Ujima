from django.contrib import admin
from Ujima.docshare.models import *
class DocumentAdmin(admin.ModelAdmin):
    list_display =('title','description','document','scribd_id',)
    search_fields = ('title',)
    
admin.site.register(Document,DocumentAdmin)
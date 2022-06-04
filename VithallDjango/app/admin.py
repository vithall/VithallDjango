from django.contrib import admin
from .models import ADSBInfo, ADSBImg
from import_export.admin import ImportExportModelAdmin
from .resource import ADSBInfoResource

#class ADSBInfoAdmin(admin.ModelAdmin):

class ADSBInfoAdmin(ImportExportModelAdmin):
    resource_class = ADSBInfoResource
    list_display = ['HexID', 'Flag', 'Type']
        
class ADSBImgAdmin(admin.ModelAdmin):
    list_display = ['Type', 'img']
    
admin.site.register(ADSBInfo,ADSBInfoAdmin)
admin.site.register(ADSBImg,ADSBImgAdmin)
    


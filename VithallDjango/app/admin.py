from django.contrib import admin
from .models import ADSBInfo, ADSBImg
from import_export.admin import ImportExportModelAdmin
from .resource import ADSBInfoResource

#class ADSBInfoAdmin(admin.ModelAdmin):

#在后台管理页面定义ADSBInfo，并显示四个字段
class ADSBInfoAdmin(ImportExportModelAdmin):
    resource_class = ADSBInfoResource
    list_display = ['HexID', 'Flag', 'Type' , 'Leixing']
 
#在后台管理页面定义ADSBImg，并显示两个字段
class ADSBImgAdmin(admin.ModelAdmin):
    list_display = ['Type', 'img']
    
#在后台管理页面中注册ADSBInfo、ADSBImg，并显示上方两个类
admin.site.register(ADSBInfo,ADSBInfoAdmin)
admin.site.register(ADSBImg,ADSBImgAdmin)
    


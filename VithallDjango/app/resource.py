from import_export import resources
from .models import ADSBInfo

class ADSBInfoResource(resources.ModelResource):

    class Meta:
        model = ADSBInfo
        #定义导入字段
        fields = ('HexID', 'Flag', 'Callsign', 'Registration', 'Type','Leixing')
        #定义导出字段
        export_order = ('HexID', 'Flag', 'Callsign', 'Registration', 'Type','Leixing')
        #排除字段，导入数据的Excel里应该是没有id的
        exclude = ['id']
        #设置主键字段，如果有地址码重复的情况，则更新已有的字段，而不会导致地址码重复
        import_id_fields = ['HexID']

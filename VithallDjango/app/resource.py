from import_export import resources
from .models import ADSBInfo

class ADSBInfoResource(resources.ModelResource):

    class Meta:
        model = ADSBInfo
        #���嵼���ֶ�
        fields = ('HexID', 'Flag', 'Callsign', 'Registration', 'Type',)
        #���嵼���ֶ�
        export_order = ('HexID', 'Flag', 'Callsign', 'Registration', 'Type',)
        #�ų��ֶΣ��������ݵ�Excel��Ӧ����û��id��
        exclude = ['id']
        #���������ֶΣ�����е�ַ���ظ����������������е��ֶΣ������ᵼ�µ�ַ���ظ�
        import_id_fields = ['HexID']

"""
Definition of models.
"""
from email.policy import default
from django.db import models

# Create your models here.
class ADSBInfo(models.Model):
    HexID = models.CharField(max_length=20, blank=False, unique=True)
    Flag = models.CharField(max_length=20,  null=True)
    Callsign = models.CharField(max_length=20,  null=True)
    Registration = models.CharField(max_length=20,  null=True)
    Type = models.CharField(max_length=20,  blank=True, null=True)
    def __str__(self):
        return "%d" % self.pk

class ADSBImg(models.Model):
    Type = models.CharField(max_length=20,  primary_key=True)
    img = models.ImageField(upload_to = 'img/', default = 'img/DefaultAircraft.png', null=True)





#切换为Mysql数据库的对应模型
#class Message(models.Model):
#    username=models.CharField(max_length=20,verbose_name="姓名")
#    password=models. CharField(verbose_name="密码")
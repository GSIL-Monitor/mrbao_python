from django.db import models

# Create your models here.
class Product(models.Model):
    productname=models.CharField(max_length=64,verbose_name="项目名称")
    productdesc=models.CharField(max_length=200,verbose_name="项目描述")
    producter=models.CharField(max_length=200,verbose_name="项目负责人")
    create_time=models.DateTimeField(auto_now=True,verbose_name="创建时间")
    prpducter_version=models.CharField(max_length=20,verbose_name="项目版本",default='v1.0')
    producter_tester=models.CharField(max_length=50,verbose_name="项目测试人员",default="mrbao")
    producter_state=models.BooleanField(default=1)

    def __str__(self):
        return self.productname


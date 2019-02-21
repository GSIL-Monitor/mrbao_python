from django.db import models
from apitest.models import Modules
# Create your models here.
class Bug(models.Model):
    #modules = models.ForeignKey(Modules, on_delete=models.CASCADE, null=True)  # 关联模块
    bug_name = models.CharField(max_length=100, verbose_name="bug名称")
    bug_desc = models.CharField(max_length=200, verbose_name="bug描述")
    BUG_STATUS = (("激活", "激活"), ("已解决", "已解决"), ("已关闭", "已关闭"))
    bug_status = models.CharField(choices=BUG_STATUS, default="激活", max_length=200, null=True, verbose_name="解决状态")
    BUG_LEVEL = (('1', '1'), ('2', '2'), ('3', '3'))
    bug_level = models.CharField(choices=BUG_LEVEL, default=3, max_length=200, null=True, verbose_name="严重程度")
    bug_creater = models.CharField(max_length=200, verbose_name="创建人")
    bug_assign = models.CharField(max_length=200, verbose_name="分配给")
    crete_time = models.DateField(auto_now=True, verbose_name="创建时间")

    def __str__(self):
        return self.bug_name
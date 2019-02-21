from django.db import models


# Create your models here.
class Product(models.Model):
    '''项目'''
    # id=models.AutoField(primary_key=False)
    product_name = models.CharField(max_length=64, verbose_name="项目名称")
    product_desc = models.CharField(max_length=200, verbose_name="项目描述")
    producter = models.CharField(max_length=200, verbose_name="项目负责人")
    create_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")
    prpducter_version = models.CharField(max_length=20, verbose_name="项目版本", null=True)
    producter_tester = models.CharField(max_length=50, verbose_name="项目测试人员")
    producter_state = models.BooleanField(default=1)

    def __str__(self):
        return self.product_name


class Modules(models.Model):
    '''项目模块'''
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product)  # 关联项目id
    module_name = models.CharField(max_length=100, verbose_name="模块名称")
    module_tester = models.CharField(max_length=50, verbose_name="模块测试人员")
    module_developer = models.CharField(max_length=50, verbose_name="模块开发人员")
    module_status = models.BooleanField()
    module_desc = models.CharField(max_length=300, verbose_name="模块描述", null=True)

    def __str__(self):
        return self.module_name


class Modules_Interface(models.Model):
    '''模块接口'''
    id = models.AutoField(primary_key=True)
    module = models.ForeignKey(Modules)  # 项目模块ID
    api_name = models.CharField(max_length=50, verbose_name="接口名")
    api_url = models.CharField(max_length=100, verbose_name="接口地址")
    api_canshu = models.CharField(max_length=100, verbose_name="接口参数")
    #api_response = models.CharField(max_length=200, verbose_name="接口返回值")
    api_desc = models.CharField(max_length=200, verbose_name="接口说明")

    def __str__(self):
        return self.api_name


class Single_interface(models.Model):
    '''单一接口'''

    single_interface = models.ForeignKey(Modules_Interface)  # 作为模块接口外键
    single_interface_name = models.CharField(max_length=100, verbose_name="接口用例标题")
    single_interface_url = models.CharField(max_length=100, verbose_name="接口地址")
    single_interface_paragram = models.CharField(max_length=100, verbose_name="接口请求参数")
    single_interface_desc = models.CharField(max_length=100, verbose_name='用例说明', null=True)
    REQUEST_METHOD = (('0', 'get'), ('1', 'post'), ('2', 'put'), ('3', 'delete'), ('4', 'patch'))

    single_interface_method = models.CharField(choices=REQUEST_METHOD, verbose_name="请求方法", default=0, max_length=200)
    #single_interface_result = models.CharField(max_length=200, verbose_name="预期结果")
    #single_interface_status = models.BooleanField(verbose_name="是否通过")
    create_time = models.DateField(auto_now=True, verbose_name="创建时间")

    class meta:
        verbose_name = "单一场景接口"
        verbose_name_plural = "单一场景接口"

    def __str__(self):
        return self.single_interface_name


class Apitest(models.Model):
    '''业务流程'''
    apitest = models.ForeignKey(Modules)
    apitestname = models.CharField(max_length=80, verbose_name="流程用例名")
    apitestdesc = models.CharField(max_length=100, verbose_name="流程描述")
    apitester = models.CharField(max_length=80, verbose_name="测试执行人")
    apitestresult = models.CharField(max_length=200, default=200)  # "流程接口预期结果"
    apiteststatus = models.BooleanField(default=1)  # 测试结果是否通过
    create_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "流程场景接口"
        verbose_name_plural = "流程场景接口"

    def __str__(self):
        return self.apitestname


class Apistep(models.Model):
    '''流程接口'''
    apitest = models.ForeignKey(Apitest)
    # module_interface=models.ForeignKey(Modules_Interface)
    apiname = models.CharField(max_length=100, verbose_name="接口名称")
    apiurl = models.CharField(max_length=200, verbose_name="接口url")
    apiparamvalue = models.CharField(max_length=800, verbose_name="请求参数和值")
    REQUEST_METHOD = (('get', 'get')), (('post', 'post')), (('put', 'put')), (('delete', 'delete'))
    apimethod = models.CharField(verbose_name="请求方法", choices=REQUEST_METHOD, default='get', max_length=200, null=True)
    apiresult = models.CharField(verbose_name="预期结果", max_length=200)
    apistatus = models.BooleanField(verbose_name="测试结果是否通过")
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now=True)  # 自动获取当前时间

    def __str__(self):
        return self.apiname


class Enveronment(models.Model):
    '''环境配置'''
    id = models.AutoField(primary_key=True)
    evn_name = models.CharField(max_length=100, verbose_name='环境名称')
    evn_ip = models.CharField(max_length=200, verbose_name='Ip地址')
    evn_port = models.CharField(max_length=100, verbose_name='端口号')
    evn_desc = models.CharField(max_length=100, verbose_name="环境描述")

    def __str__(self):
        return self.evn_name


class Database(models.Model):
    '''数据库配置'''
    db_name = models.CharField(max_length=100, verbose_name="数据库名称")
    db_ip = models.CharField(max_length=80, verbose_name="数据库IP地址")
    db_port = models.IntegerField(verbose_name="数据库端口")
    db_user = models.CharField(max_length=60, verbose_name="数据库登陆名")
    db_password = models.CharField(max_length=100, verbose_name="数据库登陆密码")
    db_desc = models.CharField(max_length=200, verbose_name="数据库描述")


# 设置
class Set(models.Model):
    id = models.AutoField(primary_key=True)
    set_name = models.CharField(max_length=100, verbose_name="设置名")
    set_value = models.CharField(max_length=100, verbose_name="设置值")

    def __str__(self):
        return self.set_name

#sql管理
class Sql_admin(models.Model):
    id = models.AutoField(primary_key=True)
    sql_name=models.CharField(max_length=200,verbose_name="sql名")
    sql_content=models.CharField(max_length=500,verbose_name="sql语句")
    create_time=models.DateTimeField(auto_now=True)
    update_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sql_name

#token
class Token(models.Model):
    id = models.AutoField(primary_key=True)
    user_mobile=models.CharField(max_length=100,verbose_name="用户手机号")
    user_token=models.CharField(max_length=100,verbose_name="用户token")
    def __str__(self):
        return self.user_mobile

#测试报告
class Report(models.Model):
    id=models.AutoField(primary_key=True)
    case_executor=models.CharField(max_length=100,verbose_name="测试执行人")
    case_success=models.CharField(max_length=100,verbose_name="用例通过数")
    case_fail=models.CharField(max_length=100,verbose_name="用例失败数")
    case_count=models.CharField(max_length=100,verbose_name="用例总数")
    report_html=models.CharField(max_length=200,verbose_name='报告')
    def __str__(self):
        return self.case_executor
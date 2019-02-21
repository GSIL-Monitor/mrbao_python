from django.contrib import admin

from apitest.models import Product,Apistep,Apitest,Modules,Modules_Interface,Single_interface


# Register your models here.

#yilou yilouapp123456
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','product_desc','producter','create_time','prpducter_version','producter_tester','producter_state']

admin.site.register(Product,ProductAdmin)

class ModulesAdmin(admin.ModelAdmin):
    list_display = ['module_name','module_tester','module_developer','module_status','module_desc','id','product_id']
admin .site.register(Modules,ModulesAdmin)

class Single_interfaceAdmin(admin.TabularInline):
    list_display = ['single_interface_id','single_interface_name','single_interface_paragram','single_interface_desc','single_interface_result','single_interface_status','create_time','id']
    model = Single_interface
    extra = 1
#项目接口
class  Modules_InterfaceAdmin(admin.ModelAdmin):
    list_display = ['api_name','api_url','api_canshu','api_desc','module_id']
    inlines = [Single_interfaceAdmin]

admin.site.register(Modules_Interface,Modules_InterfaceAdmin)


class ApistepAdmin(admin.TabularInline):
    list_display = ['apiname', 'apiurl', 'apiparamvalue', 'apimethod', 'apiresult', 'apistatus', 'create_time','id',
                    'apitest_id']
    model = Apistep
    extra = 1

class ApitestAdmin(admin.ModelAdmin):
    list_display = ['apitestname', 'apitester',  'create_time', 'apitestdesc', 'apitester','id','apitest_id']
    inlines = [ApistepAdmin]

admin.site.register(Apitest,ApitestAdmin)


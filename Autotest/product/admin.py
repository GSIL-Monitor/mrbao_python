from django.contrib import admin
from product.models import Product


# Register your models here.

class ProtuctAdmin(admin.ModelAdmin):
    list_display = ['productname','productdesc','producter','create_time','prpducter_version','producter_tester','producter_state','id']

admin.site.register(Product,ProtuctAdmin)

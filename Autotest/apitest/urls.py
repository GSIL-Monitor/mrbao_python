from django.conf.urls import url
from apitest import view_api
urlpatterns = [
    #apitest system interface
    #ex:/api/select_interface_case/
    url(r'select_module_interface/',view_api.select_module_interface),#查询模块接口
    url(r'single_interface_case/',view_api.single_interface_case),#查询单一接口
]
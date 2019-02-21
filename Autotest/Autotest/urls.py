"""Autotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from apitest import views
from bug import views as bug_views
from apitest import setviews as set
from apitest import view_api
from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'users',view_api.UserViewSet)
router.register(r'groups',view_api.GroupViewSet)
router.register(r'module_interface1',view_api.Interface_Case)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login),
    url(r'^home/', views.home),  # 主页面
    url(r'^welcome/', views.welcome),  # 右菜单主页面
    url(r'^left/', views.left),  # 左菜单
    url(r'^logout/', views.logout),
    # 产品
    url(r'^product_manage/', views.product_manage),  # 产品列表
    url(r'^add_product/', views.add_product),  # 添加
    url(r'^product/(\d+)/change/$', views.change_product),  # 修改项目
    url(r'^product/(\d+)/delete/', views.del_product),  # 删除项目
    url(r'^add/', views.add),  # 新增项目
    # 模块
    url(r'^module_page/', views.module_page),  # 模块列表
    url(r'^module/(\d+)/change/$', views.change_module),  # 修改模块
    url(r'^module/(\d+)/delete/$',views.del_module),#删除模块
    url(r'^add_module/', views.add_module),  # 添加模块
    # 模块接口
    url(r'^module_interface/', views.module_interface),  # 模块接口列表
    url(r'^add_module_interface/', views.add_module_interface),  # 新增模块接口
    url(r'^module/(\d+)/delete/',views.del_module_interface),#删除模块接口
    # 添加接口测试用例
    url(r'^single_interface_manage/', views.single_interface_manage),  # 单一接口列表
    url(r'^add_single_interface/', views.add_single_interface),  # 添加单一接口用例
    url(r'^single/(\d+)/change/', views.change_single_interface),  # 修改单一接口列表
    url(r'^single_interface/(\d+)/delete/$', views.change_product),  # 修改单一接口列表
    url(r'^apitest_manage/', views.apitest_manage),  # 接口流程列表
    url(r'^apistep_manage/', views.apistep_manage),  # 接口流程测试步骤
    url(r'^enveronment_manage/', views.enveronment_manage),  # 环境列表
    url(r'^bug_manage/', bug_views.bug_manage),  # bug列表
    url(r'^set_manage/', views.set_manage),  # 配置设置
    url(r'^set_user/', set.set_user),  # 用户管理
    url(r'^sql_manage/',views.sql_manage),#sql管理
    # 搜索
    url(r'^apisearch/', views.apisearch),  # 产品搜索设置
    url(r'^product_search/', views.product_search),  # 产品搜索
    url(r'^module_search/', views.module_search),  # 模块搜索设置
    # 显示环境列表
    url(r'^enveronment_manage/', set.enveronment_manage),
    url(r'^add_enveronment/', set.add_enveronment),
    # 数据库配置
    url(r'^db_manage/', set.db_manage),  # 显示数据库配置列表
    url(r'add_db/', set.add_db),  # 新增数据库配置

    url(r'api/',include('apitest.urls',namespace='apitest')),#配置二级接口目录

    url(r'^',include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]

from django.shortcuts import render
from  apitest.models import Product
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apitest.models import Product, Modules, Modules_Interface, Single_interface, Apitest, Apistep, Enveronment, \
    Database, Set, Sql_admin
from bug.models import Bug

from django.contrib.auth.models import User, Group
from apitest.serializers import UserSerializer, GroupSerializer
from rest_framework import status, viewsets, settings, permissions


# Create your views here.
# 登录页面
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        # if username=='admin' and password=='admin123':
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            response = HttpResponseRedirect('/home/')
            request.session['user'] = username
            return response
        else:
            return render(request, 'login.html', {'error': 'username or password error'})
    else:
        return render(request, 'login.html')


# 产品列表
def product_manage(request):
    username = request.session.get('user', '')
    product_list = Product.objects.all()
    product_count = Product.objects.all().count()  # 统计产品数
    paginator = Paginator(product_list, 10)  # 生成paginator对象，设置每页显示10条记录
    page = request.GET.get('page', 1)  # 获取当前的页码数，默认未第一页
    currentPage = int(page)  # 把获取到的当前页面数转换成整数类型
    try:
        product_list = paginator.page(page)  # 获取当前页码的记录列表
    except  PageNotAnInteger:
        product_list = paginator.page(1)  # 如果输入的页码不是整数则显示第一页内容
    except EmptyPage:
        product_list = paginator.page(paginator.num_pages)
    return render(request, 'product_manage.html',
                  {'user': username, 'products': product_list, 'productcounts': product_count})


def home(request):
    return render(request, 'home.html')


def left(request):  # 左菜单
    return render(request, 'left.html')


def welcome(request):  # 右菜单
    product_count = Product.objects.all().count()

    module_count = Modules.objects.all().count()

    module_interface = Modules_Interface.objects.all().count()
    bug_count = Bug.objects.all().count()
    return render(request, 'welcome.html', {'product_counts': product_count,
                                            'module_counts': module_count,
                                            'module_interfaces': module_interface,
                                            'bug_counts': bug_count
                                            })


# 环境配置
def enveronment_manage(request):
    username = request.session.get('user', '')
    enveronment_list = Enveronment.objects.all()
    return render(request, 'enveronment_manage.html', {'user': username, 'enveronments': enveronment_list})


# 系统设置
def set_manage(request):
    username = request.session.get('user', '')
    set_list = Set.objects.all()
    return render(request, 'set_manage.html', {'user': username, 'sets': set_list})


# 登出
def logout(request):
    auth.logout(request)
    return render(request, 'login.html')


def add(request):
    return render(request, 'Product.html')


# 添加产品
def add_product(request):
    if request.method == "GET":
        product_list = Product.objects.all()
        return render(request, 'product_manage.html', {"products": product_list})
    if request.method == 'POST':
        product_name = request.POST.get('product_name', '')  # 项目名称
        producter = request.POST.get('producter', '')  # 项目负责人
        prducter_version = request.POST.get('prpducter_version', '')
        producter_tester = request.POST.get('producter_tester', '')  # 项目测试人员
        create_time = request.POST.get('create_time', '')  # 创建时间
        product_desc = request.POST.get('product_desc', '')  # 项目描述
        producter_state = request.POST.get('producter_state', '')  # 项目状态
        # 方法一
        # result = Product.objects.create(product_name=product_name, producter=producter, create_time=create_time
        # , product_desc=product_desc, producter_state=producter_state
        # , prducter_version=prducter_version, producter_tester=producter_tester)
        # 方法二
        result = Product()
        result.product_name = product_name
        result.producter = producter
        result.prpducter_version = prducter_version
        result.producter_tester = producter_tester
        result.create_time = create_time
        result.product_desc = product_desc
        result.producter_state = producter_state
        result.save()
    product_list = Product.objects.all()
    return render(request, 'product_manage.html', {"products": product_list})


# 修改产品
@login_required
def change_product(request, id):
    ''''''
    if request.method == 'GET':
        product_list = Product.objects.get(id=id)
        return render(request, 'change_product.html', {'product_list': product_list})
    else:
        edit_id = request.POST.get('id')
        product_name = request.POST.get('product_name', '')  # 项目名称
        producter = request.POST.get('producter', '')  # 项目负责人
        # prducter_version = request.POST.get('prpducter_version', '')
        producter_tester = request.POST.get('producter_tester', '')  # 项目测试人员
        create_time = request.POST.get('create_time', '')  # 创建时间
        product_desc = request.POST.get('product_desc', '')  # 项目描述
        producter_state = request.POST.get('producter_state', '')  # 项目状态
        Product.objects.filter(id=id).update(product_name=product_name, producter=producter,
                                             producter_tester=producter_tester, create_time=create_time,
                                             product_desc=product_desc,
                                             producter_state=producter_state)
        product_list = Product.objects.all().order_by()
        return render(request, 'product_manage.html', {"products": product_list})


# 删除产品
@login_required
def del_product(request, id):
    del_product_list = Product.objects.get(id=id)
    del_product_list.delete()
    product_list = Product.objects.all()
    return render(request, 'product_manage.html', {"products": product_list})


# 产品列表搜索功能
@login_required
def product_search(request):
    username = request.session.get('user', '')
    search_productname = request.GET.get(' product_name', '')
    product_list = Product.objects.filter(product_name__icontains=search_productname)
    return render(request, 'product_manage.html', {'user': username, 'products': product_list})


# 模块列表
def module_page(request):
    module_list = Modules.objects.all()
    product_data = Product.objects.all().values('id', 'product_name')
    module_count = Modules.objects.all().count()  # 统计模块数
    paginator = Paginator(module_list, 10)  # 生成paginator对象，设置每页显示10条记录
    page = request.GET.get('page', 1)  # 获取当前的页码数，默认未第一页
    currentPage = int(page)  # 把获取到的当前页面数转换成整数类型
    try:
        module_list = paginator.page(page)  # 获取当前页码的记录列表
    except  PageNotAnInteger:
        module_list = paginator.page(1)  # 如果输入的页码不是整数则显示第一页内容
    except EmptyPage:
        module_list = paginator.page(paginator.num_pages)
    return render(request, 'module_manage.html',
                  {'modules': module_list, 'modulecounts': module_count, 'products': product_data})


# 添加模块
@login_required
def add_module(request):
    if request.method == 'GET':
        product_list = Product.objects.all()
        return render(request, 'add_module.html', {'products': product_list})
    else:
        module_name = request.POST.get('module_name', '')  # 模块名
        module_tester = request.POST.get('module_tester', '')  # 模块测试人员
        module_developer = request.POST.get('module_developer', '')  # 模块开发人员
        module_status = request.POST.get('module_status', '')  # 模块状态
        module_desc = request.POST.get('module_desc', '')  # 模块描述
        product_id = request.POST.get('product_id_list', '')
        result = Modules.objects.create(module_name=module_name, module_tester=module_tester,
                                        module_developer=module_developer,
                                        module_status=module_status, module_desc=module_desc, product_id=product_id
                                        )
        result.save()
        module_list = Modules.objects.all()
        product_data = Product.objects.all().values('id', 'product_name')
        return render(request, 'module_manage.html', {'modules': module_list, 'products': product_data})


# 修改模块
def change_module(request, id):
    if request.method == 'GET':
        module = Modules.objects.get(id=id)
        return render(request, 'change_module.html', {'modules': module})
    else:
        module_name = request.POST.get('module_name', '')
        module_tester = request.POST.get('module_tester', '')
        module_developer = request.POST.get('module_developer', '')
        module_status = request.POST.get('module_status', '')
        module_desc = request.POST.get('module_desc', '')
        Modules.objects.filter(id=id).update(module_name=module_name, module_tester=module_tester,
                                             module_developer=module_developer,
                                             module_status=module_status, module_desc=module_desc)
        module_list = Modules.objects.all()
        return render(request, 'module_manage.html', {'modules': module_list})


# 删除模块
def del_module(request, id):
    Modules.objects.get(id=id).delete()
    module_list = Modules.objects.all()
    product_data = Product.objects.all().values('id', 'product_name')
    module_count = Modules.objects.all().count()  # 统计模块数
    paginator = Paginator(module_list, 10)  # 生成paginator对象，设置每页显示10条记录
    page = request.GET.get('page', 1)  # 获取当前的页码数，默认未第一页
    currentPage = int(page)  # 把获取到的当前页面数转换成整数类型
    try:
        module_list = paginator.page(page)  # 获取当前页码的记录列表
    except  PageNotAnInteger:
        module_list = paginator.page(1)  # 如果输入的页码不是整数则显示第一页内容
    except EmptyPage:
        module_list = paginator.page(paginator.num_pages)
    return render(request, 'module_manage.html',
                  {'modules': module_list, 'modulecounts': module_count, 'products': product_data})


# 模块列表搜索
@login_required
def module_search(request):
    search_modulename = request.GET.get('module_name', '')
    module_list = Modules.objects.filter(module_name__icontains=search_modulename)
    return render(request, 'module_manage.html', {'modules': module_list})


# 删除模块接口
def del_module_interface(request, id):
    Modules_Interface.objects.get(id=id).delete()
    module_data = Modules.objects.all().values('id', 'module_name', 'product_id')  # 模块列表
    product_data = Product.objects.all().values('id', 'product_name')  # 产品列表
    module_interface_count = Modules_Interface.objects.all().count()  # 统计模块数
    module_inteaface_list = Modules_Interface.objects.all()  # 模块金额口列表
    paginator = Paginator(module_inteaface_list, 10)  # 生成paginator对象，设置每页显示10条记录
    page = request.GET.get('page', 1)  # 获取当前的页码数，默认未第一页
    currentPage = int(page)  # 把获取到的当前页面数转换成整数类型
    try:
        module_inteaface_list = paginator.page(page)  # 获取当前页码的记录列表
    except  PageNotAnInteger:
        module_inteaface_list = paginator.page(1)  # 如果输入的页码不是整数则显示第一页内容
    except EmptyPage:
        module_inteaface_list = paginator.page(paginator.num_pages)
    return render(request, 'module_interface.html',
                  {'module_interfaces': module_inteaface_list, 'Modules_Interfacecounts': module_interface_count,
                   'modules': module_data,
                   'products': product_data})


# 模块接口列表
@login_required
def module_interface(request):
    module_inteaface_list = Modules_Interface.objects.all()  # 模块金额口列表
    module_data = Modules.objects.all().values('id', 'module_name', 'product_id')  # 模块列表
    product_data = Product.objects.all().values('id', 'product_name')  # 产品列表
    module_interface_count = Modules_Interface.objects.all().count()  # 统计模块数
    paginator = Paginator(module_inteaface_list, 10)  # 生成paginator对象，设置每页显示10条记录
    page = request.GET.get('page', 1)  # 获取当前的页码数，默认未第一页
    currentPage = int(page)  # 把获取到的当前页面数转换成整数类型
    try:
        module_inteaface_list = paginator.page(page)  # 获取当前页码的记录列表
    except  PageNotAnInteger:
        module_inteaface_list = paginator.page(1)  # 如果输入的页码不是整数则显示第一页内容
    except EmptyPage:
        module_inteaface_list = paginator.page(paginator.num_pages)
    return render(request, 'module_interface.html',
                  {'module_interfaces': module_inteaface_list, 'Modules_Interfacecounts': module_interface_count,
                   'modules': module_data,
                   'products': product_data})


# 新增模块接口
@login_required
def add_module_interface(request):
    if request.method == "GET":
        module_list = Modules.objects.all()
        return render(request, 'add_module_interface.html', {'modules': module_list})
    else:
        api_name = request.POST.get('api_name', '')
        api_url = request.POST.get('api_url', '')
        api_canshu = request.POST.get('api_canshu', '')
        # api_response = request.POST.get('api_response', '')
        api_desc = request.POST.get('api_desc', '')
        module_id = request.POST.get('module_interface_list', '')
        result = Modules_Interface.objects.create(api_name=api_name, api_url=api_url, api_canshu=api_canshu,
                                                  api_desc=api_desc, module_id=module_id
                                                  )
        result.save()
        module_interface_list = Modules_Interface.objects.all()
        module_data = Modules.objects.all().values('id', 'module_name', 'product_id')  # 模块列表
        product_data = Product.objects.all().values('id', 'product_name')  # 产品列表
        return render(request, 'module_interface.html',
                      {'module_interfaces': module_interface_list, 'modules': module_data,
                       'products': product_data})


# 模块接口搜索
@login_required
def module_interface_search(request):
    search_module_interface_name = request.GET.get('module_interface_name', '')
    module_interfaces_list = Modules_Interface.objects.filter(
        module_interface_name__icontains=search_module_interface_name)
    return render(request, 'module_interface.html', {'module_interfaces': module_interfaces_list})


# 单一接口测试用例列表
@login_required
def single_interface_manage(request):
    username = request.session.get('user', '')
    single_interface_list = Single_interface.objects.all()  # 读取单一接口测试列表
    module_interface_list = Modules_Interface.objects.all().values('id', 'api_name')

    single_interface_count = Single_interface.objects.all().count()  # 统计模块数
    paginator = Paginator(single_interface_list, 10)  # 生成paginator对象，设置每页显示10条记录
    page = request.GET.get('page', 1)  # 获取当前的页码数，默认未第一页
    currentPage = int(page)  # 把获取到的当前页面数转换成整数类型
    try:
        single_interface_list = paginator.page(page)  # 获取当前页码的记录列表
    except  PageNotAnInteger:
        single_interface_list = paginator.page(1)  # 如果输入的页码不是整数则显示第一页内容
    except EmptyPage:
        single_interface_list = paginator.page(paginator.num_pages)
    return render(request, 'single_interface_manage.html',
                  {'user': username, 'single_interfaces': single_interface_list,
                   'single_interface_managecounts': single_interface_count, 'module_interfaces': module_interface_list})


# 新增单一接口用例
def add_single_interface(request):
    ''''''
    if request.method == 'GET':
        module_interface_list = Modules_Interface.objects.all()
        return render(request, 'add_single_interface_test_case.html', {'module_interfaces': module_interface_list})
    else:
        single_interface_name = request.POST.get('single_interface_name', '')  # 用例名称
        single_interface_url = request.POST.get('single_interface_url', '')  # 接口url
        single_interface_paragram = request.POST.get('single_interface_paragram', '')  # 接口参数
        single_interface_method = request.POST.get('single_interface_method', '')  # 接口方法
        # single_interface_result = request.POST.get('single_interface_result', '')  # 运行结果
        # single_interface_status = request.POST.get('single_interface_status', '')  # 执行状态
        create_time = request.POST.get('create_time', '')
        single_interface_desc = request.POST.get('single_interface_desc', '')
        single_interface_id = request.POST.get('module_interface_list', '')  # 关联模块接口id

        result = Single_interface.objects.create(single_interface_name=single_interface_name,
                                                 single_interface_url=single_interface_url,
                                                 single_interface_paragram=single_interface_paragram,
                                                 single_interface_method=single_interface_method,
                                                 # single_interface_result=single_interface_result,
                                                 create_time=create_time,
                                                 single_interface_id=single_interface_id,
                                                 single_interface_desc=single_interface_desc
                                                 )
        result.save()
        single_interface_list = Single_interface.objects.all()
        return render(request, 'single_interface_manage.html', {'single_interfaces': single_interface_list})


def change_single_interface(request, id):
    ''''''
    if request.method == 'GET':
        single_interface = Single_interface.objects.get(id=id)
        module_interface = Modules_Interface.objects.filter().values('id', 'api_name')
        return render(request, 'change_singel_interface.html',
                      {'single_interfaces': single_interface, 'module_interfaces': module_interface})
    else:
        single_interface_name = request.POST.get('single_interface_name', '')
        single_interface_url = request.POST.get('single_interface_url', '')
        single_interface_paragram = request.POST.get('single_interface_paragram', '')
        single_interface_method = request.POST.get('single_interface_method', '')
        create_time = request.POST.get('create_time', '')
        module_interface_list = request.POST.get('module_interface_list', '')
        # single_interface_result = request.POST.get('single_interface_result', '')
        single_interface_desc = request.POST.get('single_interface_desc', '')
        Single_interface.objects.filter(id=id).update(single_interface_name=single_interface_name,
                                                      single_interface_url=single_interface_url,
                                                      single_interface_paragram=single_interface_paragram,
                                                      single_interface_method=single_interface_method,
                                                      # single_interface_result=single_interface_result,
                                                      create_time=create_time,
                                                      single_interface_id=module_interface_list,
                                                      single_interface_desc=single_interface_desc
                                                      )
        single_interface_list = Single_interface.objects.all()
        return render(request, 'single_interface_manage.html', {'single_interfaces': single_interface_list})


@login_required
def apitest_manage(request):
    apitest_list = Apitest.objects.all()  # 读取流程接口数据
    username = request.session.get('user', )
    return render(request, 'apitest_manage.html', {"user": username, "apitests": apitest_list})


# 接口流程测试步骤列表
@login_required
def apistep_manage(request):
    username = request.session.get('user', '')
    apistep_list = Apistep.objects.all()  # 读取接口流程测试步骤
    return render(request, 'apistep_manage.html', {"user": username, "apisteps": apistep_list})


# 流程接口列表搜索功能
@login_required
def apisearch(request):
    username = request.session.get('user', '')
    search_apitestname = request.GET.get("apitestname", '')
    apitest_list = Apitest.objects.filter(apitestname__icontains=search_apitestname)
    return render(request, 'apitest_manage.html', {'user': username, 'apitests': apitest_list})


# sql
def sql_manage(request):
    ''''''
    if request.method == 'GET':
        sql_list = Sql_admin.objects.all()
    else:
        sql_name = request.POST.get('sql_name', '')
        sql_content = request.POST.get('sql_content', '')
        create_time = request.POST.get('create_time', '')
        update_time = request.POST.get('update_time', '')
        result = Sql_admin.objects.create(sql_name=sql_name, sql_content=sql_content,
                                          create_time=create_time, update_time=update_time)
        result.save()
        sql_list = Sql_admin.objects.all()
    sql_list_count = Sql_admin.objects.all().count()  # 统计模块数
    paginator = Paginator(sql_list, 10)  # 生成paginator对象，设置每页显示10条记录
    page = request.GET.get('page', 1)  # 获取当前的页码数，默认未第一页
    currentPage = int(page)  # 把获取到的当前页面数转换成整数类型
    try:
        sql_list = paginator.page(page)  # 获取当前页码的记录列表
    except  PageNotAnInteger:
        sql_list = paginator.page(1)  # 如果输入的页码不是整数则显示第一页内容
    except EmptyPage:
        sql_list = paginator.page(paginator.num_pages)
    return render(request, 'sql.html',
                  {'sqls': sql_list,
                   'sql_listcounts': sql_list_count})

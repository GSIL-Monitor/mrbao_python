# -*- coding: UTF-8 -*-
from apitest.models import Set,Enveronment,Database
from django.contrib.auth.models import User
from django.shortcuts import render
#展示环境列表
def enveronment_manage(request):
    enveronment_list=Enveronment.objects.all()
    return render(request,'enveronment_manage.html',{'enveronments':enveronment_list})
#新增环境
def add_enveronment(request):
    if request.method=='GET':
        enveronment_list=Enveronment.objects.all()
        return render(request,'add_enveronment.html',{'enveronments':enveronment_list})
    else:
        evn_name=request.POST.get('evn_name','')#环境名称
        evn_ip=request.POST.get('evn_ip','')#Ip地址
        evn_port=request.POST.get('evn_port','')#端口号
        evn_desc=request.POST.get('evn_desc','')#环境描述

        result=Enveronment.objects.create(evn_name=evn_name,evn_ip=evn_ip,evn_port=evn_port,
                                          evn_desc=evn_desc
                                          )
        result.save()
        enveronment_list = Enveronment.objects.all()
        return render(request, 'enveronment_manage.html', {'enveronments': enveronment_list})

#数据库配置
def db_manage(request):
    db_list=Database.objects.all()
    return render(request,'db_manage.html',{'dbs':db_list})

def add_db(request):
    ''''''
    if request.method=="GET":
        return render(request,'add_db.html')
    else:
        db_name=request.POST.get('db_name','')#数据库名称
        db_ip=request.POST.get('db_ip','')#数据库IP地址
        db_port=request.POST.get('db_port','')#数据库端口
        db_user=request.POST.get('db_user','')#数据库登陆名
        db_password=request.POST.get('db_password','')#数据库登陆密码
        db_desc=request.POST.get('db_desc','')#数据库描述
        result=Database.objects.create(db_name=db_name,db_ip=db_ip,db_port=db_port,db_user=db_user,
                                       db_password=db_password,db_desc=db_desc )
        result.save()
        db_list = Database.objects.all()
        return render(request, 'db_manage.html', {'dbs': db_list})

#用户管理
def set_user(request):
    user_list=User.objects.all()
    username=request.session.get('user','')
    return render(request,'set_user.html',{'user':username,'users':user_list})






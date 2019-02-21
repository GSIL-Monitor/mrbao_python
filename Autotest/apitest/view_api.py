from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from apitest.models import Product, Modules, Modules_Interface, Single_interface, Apitest, Apistep, Enveronment, \
    Database, Set, Sql_admin
from django.contrib.auth.models import User, Group
from apitest.serializers import Module_interfaceSerializers, UserSerializer, GroupSerializer, \
    Single_interfaceSerializers
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response


class Interface_Case(viewsets.ModelViewSet):
    '''
    模块接口
    '''
    queryset = Modules_Interface.objects.all()
    serializer_class = Module_interfaceSerializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@api_view(['GET', 'POST'])
def select_module_interface(request):
    if request.method == 'GET':
        modules_Interface = Modules_Interface.objects.all()
        serializer = Module_interfaceSerializers(modules_Interface, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def single_interface_case(request, format=None):
    if request.method == 'GET':
        single_interface_list = Single_interface.objects.all()
        serializer = Single_interfaceSerializers(single_interface_list, many=True)

        return Response(serializer.data)

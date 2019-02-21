from apitest.models import Product, Modules_Interface, Single_interface
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class Single_interfaceSeralizers1(serializers.Serializer):
    REQUEST_METHOD = (('0', 'get'), ('1', 'post'), ('2', 'put'), ('3', 'delete'), ('4', 'patch'))
    id = serializers.IntegerField(read_only=True)
    single_interface_name = serializers.CharField(required=False, max_length=100, error_messages=
    {'required':'single_interface_name不能为空，请填写接口名'
    })
    single_interface_url = serializers.CharField(required=False, max_length=100)
    single_interface_paragram = serializers.CharField(required=False, max_length=100)
    single_interface_method = serializers.ChoiceField(choices=REQUEST_METHOD, default=0)
    create_time = serializers.DateField()

    def create(self, validated_data):
        single_interface_name = validated_data['single_interface_name']
        single_interface_url = validated_data['single_interface_url']
        single_interface_paragram = validated_data['single_interface_paragram']
        single_interface_method = validated_data['single_interface_method']
        create_time = validated_data['create_time']
        return Single_interface.objects.create(**validated_data)

    def upadte(self, instance, validated_data):
        instance.single_interface = validated_data.get('single_interface', '')
        instance.single_interface_name = validated_data.get('single_interface_name', '')
        instance.single_interface_url = validated_data.get('single_interface_url', '')
        instance.single_interface_paragram = validated_data.get('single_interface_paragram', '')
        instance.single_interface_method = validated_data.get('single_interface_method', '')
        instance.create_time = validated_data.get('create_time', '')
        instance.save()
        return instance


class ProductSerializers(serializers.HyperlinkedModelSerializer):
    '''项目'''

    class Meta:
        model = Product
        fields = "__all__"


class Module_interfaceSerializers(serializers.HyperlinkedModelSerializer):
    '''模块接口'''

    class Meta:
        model = Modules_Interface
        fields = ('api_name', 'api_url', 'api_canshu', 'api_desc')


class Single_interfaceSerializers(serializers.HyperlinkedModelSerializer):
    '''单一接口'''

    class Meta:
        model = Single_interface
        fields = ('single_interface_name', 'single_interface_url', 'single_interface_paragram', 'single_interface_desc',
                  'single_interface_method', 'create_time')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

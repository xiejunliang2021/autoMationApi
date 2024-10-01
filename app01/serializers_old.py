"""
定义drf框架的序列化器类
"""
from rest_framework import serializers
from app01.models import UserInfo, Addr


class UserInfoSerializer(serializers.Serializer):
    """定义序列化器"""
    # 后面的参数read_only=True表示只参与序列化，不参与反序列化
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    pwd = serializers.CharField(max_length=18)
    email = serializers.EmailField(max_length=28)
    age = serializers.IntegerField(min_value=0, max_value=150)


class AddrSerializer(serializers.Serializer):
    """收货地址的序列化"""
    id = serializers.IntegerField()
    mobile = serializers.CharField(max_length=18)
    city = serializers.CharField(max_length=10)
    info = serializers.CharField(max_length=200)
    # 返回关联模型对象的str定义的返回值
    user = serializers.StringRelatedField()

    class Meta:
        model = Addr
        fields = ['UserInfo_name', 'UserInfo_pwd', 'UserInfo_age']
















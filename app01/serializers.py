"""
定义drf框架的序列化器类
"""
from rest_framework import serializers
from app01.models import UserInfo, Addr


class UserInfoSerializer(serializers.ModelSerializer):
    """用户信息序列化器"""

    class Meta:
        model = UserInfo
        # 所有字段都进行序列化操作
        fields = '__all__'


class AddrSerializer(serializers.ModelSerializer):
    """用户地址序列化器"""

    class Meta:
        model = Addr
        # 序列化字段返回的信息
        fields = ['user', 'mobile', 'info']

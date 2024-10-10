"""
运用rest_framework的方式来改写view
"""
from rest_framework.permissions import IsAuthenticated
from .serializers import UserInfoSerializer
from .models import UserInfo
from rest_framework import viewsets
from rest_framework import mixins
# 限流
from rest_framework.throttling import AnonRateThrottle
# 自定义过滤器类
from .filters import UserInfoFilter


# 用户信息的增删查改
class UserView(viewsets.ReadOnlyModelViewSet, mixins.DestroyModelMixin):
    # 指定模型类查询集
    queryset = UserInfo.objects.all()

    # 指定序列化器
    serializer_class = UserInfoSerializer

    # 设置访问权限
    # permission_classes = (IsAuthenticated,)

    # 限流
    throttle_classes = (AnonRateThrottle,)

    # 方式一：直接指定过滤字段
    # filterset_fields = ['name', 'age']

    # 方式二：指定过滤器类
    filterset_class = UserInfoFilter



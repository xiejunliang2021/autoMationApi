"""
运用rest_framework的方式来改写view
"""
from .serializers import UserInfoSerializer
from .models import UserInfo
from rest_framework.viewsets import ModelViewSet


# 用户信息的增删查改
class UserView(ModelViewSet):
    # 指定模型类查询集
    queryset = UserInfo.objects.all()

    # 指定序列化器
    serializer_class = UserInfoSerializer



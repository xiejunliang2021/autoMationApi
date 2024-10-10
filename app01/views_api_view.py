"""
运用rest_framework的方式来改写view
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserInfoSerializer
from .models import UserInfo

from django.http import JsonResponse
from django.shortcuts import HttpResponse
# 导入模型
from rest_framework.parsers import JSONParser


@api_view(["GET", "POST"])
def user_list(request):
    """
    获取用户信息（get）
    :param request:
    :return:
    """
    if request.method == "GET":
        users = UserInfo.objects.all()
        # 创建序列化器，many=True 告诉当前是查询集
        ser = UserInfoSerializer(users, many=True)
        result = {
            'data': ser.data,
            'code': 200,
            'message': '用户信息获取成功！'

        }
        return Response(result, status.HTTP_200_OK)

    # 创建序列化器
    ser = UserInfoSerializer(data=request.data)
    # 校验请求参数
    if ser.is_valid():  # 如果数据校验成功则保存数据
        ser.save()

        return Response({'code': 201, 'data': ser.data, 'message': '数据保存成功'}, status=status.HTTP_201_CREATED)
    else:

        return Response({'code': 400, 'message': ser.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PATCH", "DELETE"])
def user_detail(request, id):
    """

    :param request:
    :param id:  操作资源的id
    :return:
    """
    try:
        user_obj = UserInfo.objects.get(id=id)
    except Exception as e:
        return Response("404,访问的资源不存在", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # 获取单个资源并返回
        ser = UserInfoSerializer(user_obj)

        return Response({'code': 200, 'data': ser.data, 'message': '数据获取成功'}, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        user_obj.delete()

        # 按照rest风格的设计delete返回的数据是个空对象，返回的代码是204
        return Response(status=status.HTTP_204_NO_CONTENT)

    else:
        # 传递两个参数代表修改信息
        ser = UserInfoSerializer(instance=user_obj, data=request.data)
        if ser.is_valid():
            ser.save()

            return Response({'code': 200, 'data': ser.data, 'message': '数据修改成功'}, status=status.HTTP_200_OK)
        else:
            return Response({'code': 400, 'message': ser.errors}, status=status.HTTP_400_BAD_REQUEST)







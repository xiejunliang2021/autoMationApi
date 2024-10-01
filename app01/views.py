from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
# 导入模型
from .models import UserInfo
# 导入模型序列化器
from .serializers import UserInfoSerializer
from rest_framework.parsers import JSONParser


def user_list(request):
    """
    1:获取用户信息（get）
    2:添加用户信息（post）
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
            'message': 'OK'

        }
        return JsonResponse(result)
    elif request.method == "POST":
        # 获取请求数据
        data = JSONParser().parse(request)
        # 创建序列化器
        ser = UserInfoSerializer(data=data)
        # 校验请求参数
        if ser.is_valid():     # 如果数据校验成功则保存数据
            ser.save()

            return JsonResponse({'code': 201, 'data': ser.data, 'message': '数据保存成功'}, status=201)
        else:

            return JsonResponse({'code': 400, 'message': ser.errors}, status=400)
    else:
        return JsonResponse({"code": 405, "message": "当前地址不支持该方法:{}".format(request.method)}, status=405)


def user_detail(request, id):
    """

    :param request:
    :param id:  操作资源的id
    :return:
    """
    try:
        user_obj = UserInfo.objects.get(id=id)
    except Exception as e:
        return HttpResponse("404,访问的资源不存在", status=404)
    if request.method == 'GET':
        # 获取单个资源并返回

        ser = UserInfoSerializer(user_obj)

        return JsonResponse({'code': 200, 'data': ser.data, 'message': '数据获取成功'}, status=200)

    elif request.method == 'DELETE':
        user_obj.delete()

        # 按照rest风格的设计delete返回的数据是个空对象，返回的代码是204
        return JsonResponse({}, status=204)

    elif request.method == 'PUT':
        params = JSONParser().parse(request)
        # 传递两个参数代表修改信息
        ser = UserInfoSerializer(instance=user_obj, data=params)
        if ser.is_valid():
            ser.save()

            return JsonResponse({'code': 200, 'data': ser.data, 'message': '数据修改成功'}, status=200)
        else:
            return JsonResponse({'code': 400, 'message': ser.errors}, status=400)

    else:
        return JsonResponse({"code": 405, "message": "当前地址不支持该方法:{}".format(request.method)}, status=405)

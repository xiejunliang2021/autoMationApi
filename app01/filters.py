# -*- coding: UTF-8 -*-
'''
@Project ：autoMationApi 
@File ：filters.py
@Author ：Anita_熙烨
@Date ：2024/10/10 9:51 
@JianShu : 人生在世不容易，求佛祖保佑我们全家苦难不近身，平安健康永相随，
            远离小人讹诈，万事如意，心想事成！！！
'''
from django_filters import rest_framework as filters
from app01.models import UserInfo


class UserInfoFilter(filters.FilterSet):
    """自定义过滤器类，一般过滤器为哪个模型服务就写哪个模型的filter"""
    min_age = filters.NumberFilter(field_name="age", lookup_expr='gte')
    max_age = filters.NumberFilter(field_name="age", lookup_expr='lte')

    class Meta:
        model = UserInfo
        fields = ['name', 'age']

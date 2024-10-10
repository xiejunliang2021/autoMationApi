from django.contrib import admin
from django.urls import path
from . import views
# 导入rest_fromwork中的路由，该路由只对视图集有效
from rest_framework import routers

urlpatterns = [
    # path('users/', views.user_list, name='users_list'),
    # path('users/<int:id>/', views.user_detail, name='user_list'),
]

router = routers.SimpleRouter()
router.register(r"users", views.UserView)
urlpatterns += router.urls



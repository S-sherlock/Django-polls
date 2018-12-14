"""
 . 代表当前文件夹下
 .. 代表父级文件夹下
 终端这样写：
 cd ../
 cd ./

"""

from django.urls import path
from . import views

'''先引入视图函数
   path()函数定义的路由最终都会在项目启动时加载
   path(路由规则)
'''
urlpatterns = [

    path('', views.index, name='index'),
    path('index', views.index, name='index')
]


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
app_name = 'polls'
urlpatterns = [

    # 首页 http://ip:port/polls/
    path('', views.index, name='index'),
    # 首页 问题列表/polls/index/
    path('index', views.index, name='index'),
    # 问题详情页 /polls/1/
    path('<int:question_id>/', views.detail, name='detail'),
    # 投票结果页 /polls/2/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # 去投票，选项计数加一 /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')
]


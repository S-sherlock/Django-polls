from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice


# Create your views here.
# def index(request):
#     return HttpResponse("""
#         <html>
#             <head>
#             </head>
#             <body>
#                 <h1>hello world</h1>
#             </body>
#         </html>
#     """)

def index(request):
    """
    展示问题列表
    :return: 
    """
    question_list = Question.objects.all().order_by('-pub_date')
    print(question_list)
    for q in question_list:
        print(q.id, q.question_text, q.pub_date)
        # print(q['id'])

def detail(request, question_id):
    """
    
    显示一个问题的详细信息，问题内容、选项、发布时间、投票数
    """
    pass

def results(request, question_id):
    """
    投票结果
    """
    pass

def vote(request, question_id):
    """
    投票 
    """
    pass
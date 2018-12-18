from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question, Choice
from django.template import loader



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

    另一种渲染的方法：快捷函数 render()
    def index(request):
        question_list = Question.objects.all().order_by('-pub_date')
        context = {'question_list': question_list}
        return render(request, 'polls/index.html', context)
    """

    question_list = Question.objects.all().order_by('-pub_date')
    # 1
    # print(question_list)
    # output = ''
    # for q in question_list:
    #     print(q.id, q.question_text, q.pub_date)
    #     output = output + q.question_text
    # print(output)

    # 2
    # output = ','.join([q.question_text for q in question_list])
    # return HttpResponse(output)
    template = loader.get_template('polls/index.html')
    context = {
        'question_list': question_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    """
    
    显示一个问题的详细信息，问题内容、选项、发布时间、投票数

    如果指定问题 ID 所对应的问题不存在，这个视图就会抛出一个 Http404 异常。
    django另一个快捷函数：get_object_or_404()
    from django.shortcuts import get_object_or_404, render
    """
    # try:
    #     question = Question.objects.get(id=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("404, 此问题不存在")
    # question = Question.objects.get(id=question_id)
    # context = {'question': question}
    # return render(request, 'polls/detail.html', context)
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/detail.html', {'question': question})


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
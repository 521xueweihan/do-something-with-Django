#coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(u'Hello xueweihan!!')


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def home(request):
    # return render(request, 'home.html')

    # 加上模版引擎
    test_string = '这是传递过来的字符串！'

    # 数组
    test_list = [u'香蕉', u'苹果', u'西瓜', u'嘿嘿']
    test_dict = {'Hero': u'蝙蝠侠盗',
                 'Villain': u'采花大盗'}

    # 用于练习逻辑判断的变量var
    var = 88
    return render(request,
                  'home.html',
                  {'test_list': test_list,
                   'test_string': test_string,
                   'test_dict': test_dict,
                   'var':var})

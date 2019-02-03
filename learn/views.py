# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(u"这个是一个测试页面abcdef!")
# Create your views here.

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def vadd(request):
    return render(request, 'add.html')

def home(request):
    str = u"this is a input str"
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    return render(request, 'home.html', {'string': str, 'TutorialList': TutorialList, 'info_dict': info_dict})

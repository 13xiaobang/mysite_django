# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(u"这个是一个测试页面abcdef!")
# Create your views here.
